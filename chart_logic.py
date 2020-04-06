import datetime

# get the amount per purchase category
def get_chart_data_category(transactions):
  try:    
    chartValues = dict()
    for tran in transactions:
      c = str(tran['category'])
      a = float(tran['amount'])
      if c not in chartValues.keys():
        chartValues[c] = a
      else:
        chartValues[c] += a
    return chartValues
    # TODO not sure how to sum the amount as we go in a dict comprehension, or if its possible in a dict comprehension
    # valuesComp = {str(tran['category']):float(tran['amount']) for tran in transactions}
    # print('CHART VALUES USING DICT COMPREHENSION: {}'.format(str(valuesComp)))
  except Exception as e:
    print("error occurred in get_chart_data_category()")
    print(e)
    return None

# get the amount spent per day
def get_chart_data_date(transactions):
    try:
        base = datetime.datetime.today()
        date_list = [base - datetime.timedelta(days=x) for x in range(30)]        
        dates_formatted = [d.strftime("%Y-%m-%d") for d in date_list]
        chartValues = {d:0.0 for d in dates_formatted}
        for tran in transactions:
            amt = float(tran['amount'])
            date = tran['date']
            # we are looking at the last 30 days so all trans dates should be there
            chartValues[date] += amt
        
        return chartValues
    except Exception as e:
        print("error occurred in get_chart_data_date()")
        print(e)