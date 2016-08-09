
#return true if dt1 is older than dt2
#a sample date: {'year':2013, 'month':10, 'day':20}

def is_older(dt1, dt2):
    if dt1['year'] != dt2['year']:
        return dt1['year'] < dt2['year']
    elif dt1['month'] != dt2['month']:
        return dt1['month'] < dt2['month']
    else:
        return dt1['day'] < dt2['day']
    
def test_1():
    return is_older({'year':2013, 'month':9, 'day':15}, {'year':2013, 'month':9, 'day':15}) == False

def test_2():
    return is_older({'year':2012, 'month':9, 'day':15}, {'year':2013, 'month':9, 'day':15}) == True

def test_3():
    return is_older({'year':2014, 'month':9, 'day':15}, {'year':2013, 'month':9, 'day':15}) == False

def test_4():
    return is_older({'year':2013, 'month':8, 'day':15}, {'year':2013, 'month':9, 'day':15}) == True
    
def test_5():
    return is_older({'year':2013, 'month':10, 'day':15}, {'year':2013, 'month':9, 'day':15}) == False
    

