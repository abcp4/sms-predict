# Experimentos

## Reproduzindo pipeline

```shell
pip install -r requirements.txt
dvc repro
```

2. Visualizar métricas
```shell
dvc metrics show
```


## Passo a passo pipeline

1. Preparar os dados
```shell
dvc run -n prepare \  
          -p prepare.seed,prepare.split \
          -d prepare.py -d data/raw/train_data.csv \
          -o data/prepared \
          python prepare.py data/raw/train_data.csv
```

2. Treinamento
```shell
dvc run -n train \   
          -p train.kernel,train.C \                                 
          -p train.features.max_features,train.features.ngrams \
          -d train.py -d data/prepared \          
          -o data/models/model.pkl \              
          python train.py data/prepared data/models/model.pkl
```

3. Avaliação
```shell
dvc run -n evaluate \
          -d evaluate.py -d data/models/model.pkl -d data/prepared \
          -M data/metrics/scores.json \
          --plots-no-cache data/metrics/prc.json \
          --plots-no-cache data/metrics/roc.json \
          python evaluate.py data/models/model.pkl \
                 data/prepared
```

4. Visualizar métricas
```shell
dvc metrics show
```

5. Modificar plots
```shell
dvc plots modify data/metrics/prc.json -x recall -y precision
dvc plots modify data/metrics/roc.json -x fpr -y tpr
```

6. Exibir plots
```shell
dvc plots show
```
