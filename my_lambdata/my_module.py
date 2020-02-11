def split_data(X):
  train, val = train_test_split(X, random_state=42)
  train = train.copy
  val = val.copy
  return train, val