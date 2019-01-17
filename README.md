## Term Project

### Set up environment
using the conda or pyenv

- conda create -n cs3243 python=2.7
- conda env remove --name cs3243
- source activate cs3243

replace the cs3243 with whatever name you want
https://conda.io/docs/index.html

pip install PyPokerEngine  
https://ishikota.github.io/PyPokerEngine/



testing installmement:

```
import pypokerengine   
print("hello world")
```


### Set up gui  
```pip install pypokergui```
run the command and replace the yaml file path
```
pypokergui serve /Users/ishikota/poker/poker_conf.yaml --port 8000 --speed moderate
```