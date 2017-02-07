# Import datetime library to answer the questions
import datetime

# Create function that applies to all three sets of inputs
# Takes two date inputs and converts them to Datetime objects
#   in order to subtract quickly and get number of days.
def days_answer(in1, in2, str_form):
    date_start = datetime.datetime.strptime(in1, str_form)
    date_stop = datetime.datetime.strptime(in2, str_form)
    return (date_stop - date_start)

# Print out answers

####a)
date_start1 = '01-02-2013'
date_stop1 = '07-28-2015'

print 'a)', days_answer(date_start1, date_stop1, '%m-%d-%Y')

####b)
date_start2 = '12312013'
date_stop2 = '05282015'

print 'b)', days_answer(date_start2, date_stop2, '%m%d%Y')

####c)
date_start3 = '15-Jan-1994'
date_stop3 = '14-Jul-2015'

print 'c)', days_answer(date_start3, date_stop3, '%d-%b-%Y')
