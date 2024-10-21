# Neural network model for structure factor of polymer systems
This is the source code for the paper "Neural network model for structure factor of polymer systems". 
<p align='center'>
<img src='https://cdn.jsdelivr.net/gh/HuangJiaLian/DataBase0@master/uPic/2024-10-22-00-41-mT29vs.png' width='50%'>
</p>

## Abstract
As an important physical quantity to understand the internal structure of polymer chains, the structure factor is being studied both in theory and experiment. Theoretically, the structure factor of Gaussian chains has been solved analytically, but for wormlike chains, numerical approaches are often used, such as Monte Carlo simulations, solving the modified diffusion equation. In these works, the structure factor needs to be calculated differently for different regions of the wave vector and chain rigidity, and some calculation processes are resource consuming. In this work, by training a deep neural network, we obtained an efficient model to calculate the structure factor of polymer chains, without considering different regions of wavenumber and chain rigidity. Furthermore, based on the trained neural network model, we predicted the contour and Kuhn lengths of some polymer chains by using scattering experimental data, and we found that our model can get pretty reasonable predictions. This work provides a method to obtain the structure factor for polymer chains, which is as good as previous and more computationally efficient. It also provides a potential way for the experimental researchers to measure the contour and Kuhn lengths of polymer chains.

## Citation
Cite as 

> Jie Huang, Shiben Li, Xinghua Zhang, Gang Huang; Neural network model for structure factor of polymer systems. J. Chem. Phys. 28 September 2020; 153 (12): 124902. https://doi.org/10.1063/5.0022464

Or
```
 @article{huang2020,
    author = {Huang, Jie and Li, Shiben and Zhang, Xinghua and Huang, Gang},
    title = "{Neural network model for structure factor of polymer systems}",
    journal = {The Journal of Chemical Physics},
    volume = {153},
    number = {12},
    pages = {124902},
    year = {2020},
    month = {09},
    issn = {0021-9606},
    doi = {10.1063/5.0022464},
    url = {https://doi.org/10.1063/5.0022464},
    eprint = {https://pubs.aip.org/aip/jcp/article-pdf/doi/10.1063/5.0022464/14758090/124902\_1\_online.pdf},
}
```
