families={
          'steve rogers':
                    {
                     'sam':{'bucky','natasa'},
                     'nebula':{'vision'}},
          'tchala':
                 {
                  'suri':{'tony stark'},
                  'wanda':{'pepper potts'},
                  'rdj':{'red skull'}},
          'odin':
                 {
                  'thor','odin','hela','gamora'}
          }
for parent,children in families.items():
    print(f"{parent} has {len(children)}kid(s):")
    print(f"{',and '.join([str(child) for child in [*children]])}")