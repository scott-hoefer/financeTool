def get_transactions_by_category(transactions):
  try:    
    chartValues = dict()
    for tran in transactions:
      c = str(tran['category'])
      a = float(tran['amount'])
      if c not in chartValues.keys():
        chartValues[c] = float(a)
      else:
        chartValues[c] += float(a)
    return chartValues
    # TODO not sure how to sum the amount as we go in a dict comprehension, or if its possible in a dict comprehension
    # valuesComp = {str(tran['category']):float(tran['amount']) for tran in transactions}
    # print('CHART VALUES USING DICT COMPREHENSION: {}'.format(str(valuesComp)))
  except Exception as e:
    print("error occurred when trying to create bar chart dict")
    print(e)
    return None