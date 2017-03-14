import random
import torch
import torch.nn as nn
import json
import argparse
from torch.autograd import Variable
from torch.utils.data import DataLoader
from copy import deepcopy

## Arguments

parser = argparse.ArgumentParser()

# Dataset Options
parser.add_argument('--input_h5', default='data/pass.h5')
parser.add_argument('--input_json', default='data/pass.json')
parser.add_argument('--batch_size', type=int, default=50)
parser.add_argument('--seq_length', type=int, default=50)

# Model Options
parser.add_argument('--init_from', default='')
parser.add_argument('--reset_iterations', default=1)
parser.add_argument('--model_type', default='lstm')
parser.add_argument('--wordvec_size', type=int, default=64)
parser.add_argument('--rnn_size', type=int, default=128)
parser.add_argument('--num_layers', type=int, default=2)
parser.add_argument('--dropout', type=int, default=0)
parser.add_argument('--batchnorm', type=int, default=0)
parser.add_argument('--shuffle', action='store_false')


# Optimization Options
parser.add_argument('--max_epochs', type=int, default=50)
parser.add_argument('--learning_rate', type=float, default=.002)
parser.add_argument('--grad_clip', type=int, default=5)
parser.add_argument('--lr_decay_every', type=int, default=5)
parser.add_argument('--lr_decay_factor', type=float, default=0.5)

# Output Options
parser.add_argument('--print_every', type=int, default=1)
parser.add_argument('--checkpoint_every', type=int, default=1000)
parser.add_argument('--checkpoint_name', default='cv/checkpoint')

# Benchmark Options
parser.add_argument('--speed_benchmark', type=int, default=0)
parser.add_argument('--memory_benchmark', type=int, default=0)

# Backend Options
parser.add_argument('--gpu', type=int, default=0)
parser.add_argument('--gpu_backend', default='cuda')

opt = parser.parse_args()

## Set Up GPUs

## Load the Data
loader = DataLoader(opt.input_h5, opt.batch_size, opt.shuffle)

with open(opt.input_json) as json_data:
    idx_to_token = json.load(json_data)['idx_to_token']

print(idx_to_token)

## Initialize the model and criterion
opt = Namespace(**vars(args))

opt_clone = deepcopy(opt)
opt_clone.idx_to_token = idx_to_token

model = None
start_i = 0

if opt.init_from != '':
    print('Initializing from ', opt.init_from)
    checkpoint = torch.load(opt.init_from)
    model = checkpoint.model(type = dtype) # Is this correct??
    if opt.reset_iterations == 0:
        start_i = checkpoint.i # Is this correct?
else:
    model = nn.LanguageModel(opt_clone):type(dtype) #

local params, grad_params = model.getParameters() #
local crit = nn.CrossEntropyCriterion():type(dtype) #

## Set up some variables we will use below
N, T = opt.batch_size, opt.seq_length
train_loss_history = {}
val_loss_history = {}
val_loss_history_it = {}
forward_backward_times = {}
init_memory_usage, memory_usage = None, {}

## MEMORY BENCHMARK STUFF
# if opt.memory_benchmark == 1 then
#   # This should only be enabled in GPU mode
#   assert(cutorch)
#   cutorch.synchronize()
#   local free, total = cutorch.getMemoryUsage(cutorch.getDevice())
#   init_memory_usage = total - free
# end

## Loss function that we pass to an optim method
local function f(w)
  assert(w == params)
  grad_params:zero()

  -- Get a minibatch and run the model forward, maybe timing it
  local timer
  local x, y = loader:nextBatch('train')
  x, y = x:type(dtype), y:type(dtype)
  if opt.speed_benchmark == 1 then
    if cutorch then cutorch.synchronize() end
    timer = torch.Timer()
  end
  local scores = model:forward(x)

  -- Use the Criterion to compute loss; we need to reshape the scores to be
  -- two-dimensional before doing so. Annoying.
  local scores_view = scores:view(N * T, -1)
  local y_view = y:view(N * T)
  local loss = crit:forward(scores_view, y_view)

  -- Run the Criterion and model backward to compute gradients, maybe timing it
  local grad_scores = crit:backward(scores_view, y_view):view(N, T, -1)
  model:backward(x, grad_scores)
  if timer then
    if cutorch then cutorch.synchronize() end
    local time = timer:time().real
    print('Forward / Backward pass took ', time)
    table.insert(forward_backward_times, time)
  end

  -- Maybe record memory usage
  if opt.memory_benchmark == 1 then
    assert(cutorch)
    if cutorch then cutorch.synchronize() end
    local free, total = cutorch.getMemoryUsage(cutorch.getDevice())
    local memory_used = total - free - init_memory_usage
    local memory_used_mb = memory_used / 1024 / 1024
    print(string.format('Using %dMB of memory', memory_used_mb))
    table.insert(memory_usage, memory_used)
  end

  if opt.grad_clip > 0 then
    grad_params:clamp(-opt.grad_clip, opt.grad_clip)
  end

  return loss, grad_params
end




# ## Main Script
#
# if __name__ == '__main__':
#     if args.encoding == 'bytes': args.encoding = None
#
#   # First go the file once to see how big it is and to build the vocab
#     token_to_idx = {}
#     total_size = 0
#     with codecs.open(args.input_txt, 'r', args.encoding) as f:
#     for line in f:
#         total_size += len(line)
#         for char in line:
#             if char not in token_to_idx:
#                 token_to_idx[char] = len(token_to_idx) + 1
#
#
#     # Create a list of samples
#     sample = []
#     for filename in findFiles(args.input_txt):
#         category = filename.split('/')[-1].split('.')[0]
#         all_categories.append(category)
#         lines = readLines(filename)
#         category_lines[category] = lines
#
# # Create RNN Class
# class RNN(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size):
#         super(RNN, self).__init__()
#         self.hidden_size = hidden_size
#
#         self.i2h = nn.Linear(input_size + hidden_size,
#                              hidden_size)
#         self.i2o = nn.Linear(input_size + hidden_size,
#                              output_size)
#         self.o2o = nn.Linear(hidden_size + output_size, output_size)
#         self.dropout = nn.Dropout(0.1)
#         self.softmax = nn.LogSoftmax()
#
#     def forward(self, input, hidden):
#         input_combined = torch.cat((category, input, hidden), 1)
#         hidden = self.i2h(input_combined)
#         output = self.i2o(input_combined)
#         output_combined = torch.cat((hidden, output), 1)
#         output = self.o2o(output_combined)
#         output = self.dropout(output)
#         output = self.softmax(output)
#         return output, hidden
#
#     def initHidden(self):
#         return Variable(torch.zeros(1, self.hidden_size))
#
# # Random item from a list
# def randomChoice(l):
#     return l[random.randint(0, len(l) - 1)]
#
# # Get a random sample
# def randomSample():
#     randsamp = randomChoice()
#     return line