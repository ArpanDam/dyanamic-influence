This is the code for DNInf - a method to find topic aware dyanamic influencer for each snapshot.

**How to run the DynTriad.py **


    conda create --name myenv python=3.6  **## Creating venv**
    
    conda activate myenv  **## Activate**
    
    pip install -r requirements.txt   **## Install dependencies**
    
    python setup.py install     **## Setup**
    
    python DynTriad.py            **## Run**
    
    example: D:\python_lib\DynamicGEM-master\Testing\dynamicgem-master2\dynamicgem-master\Graph10_v2_ta\formatted   **## Enter graph  full path**
    
    Graph10_v2_ta\formatted    **## For sample there is dummy graph in path**  formatted folder contains the input snapshots. Each entry corresponds to nodeid. probability and embedding of topics

    After running the code a output folder will be genretrated containing the embedding of all the nodes at every snapshot. the path will be: output\sbm_cd
    
**Ouput embedding of largest copmonent **


      Sample Output folder contains the embedding of 11,492 nodes for 9 snapshots. A tsne.py file is also provided to analyse the embdding of nodes of each snapshots.
      
      Run the tsne.py to visualise the nodes embedding for each snapshot.  
      
      The nodes in the sample output correspond to one of the largest connected components of Meetup dataset.

**Finding top k influencers and top r badges**

        Seed and badge finder contains the code for finding top k influencers and top r badges
        
        seed_finder.py finds the k best influencers. badge_finder.py finds the r best badges for the k best influencer.
        
        Run `python badge_finder.py' to find top 5 influencial members and top 2 influence badges.
        
        Run `python badge_finder.py number_of_influencial_users number_of_influence_badges' to get the output as top-k influencial nodes and top-r influence badges.


