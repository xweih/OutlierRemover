# Outlier Remover
A routine that removes the outliers of a dataset until there is none left.

```ruby
def clean_mean_auto(sample, cutoff):

    new = []
    old = sample
    
    while old != new:
        old = sample                                
        data_mean = np.mean(old) 
        data_std = np.std(old)
        cut_off_val = data_std * cutoff
        lower = data_mean - cut_off_val
        upper = data_mean + cut_off_val
        new = [x for x in old if x >= lower and x <= upper]  
        sample = new
        
    print(new)
    
    return round(np.mean(new),2)
    
```

