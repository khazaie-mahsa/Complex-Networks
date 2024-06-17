# Gintropy Implementation

This implementation is based on Biró et al[1].

## Results

| Network                             | Network Size | Properties | Gini Index | Gintropy |
| ----------------------------------- | ------------ | ---------- | ---------- | -------- |
| Regular (Communism)                 | 100          | -          | 0          | 0        |
| ER (Natural)                        | 100          | p = 0.1    | 0.1653     | 0.109    |
| Random degree sequence (Eco-window) | 100          | a=1, b=10  | 0.2924     | 0.2187   |
| BA (Capitalism)                     | 100          | m=5        | 0.3009     | 0.2311   |

Average Gini and Gintropy for 100 simulations

| Network                                  | Network Size                | Properties | Avg Gini Index | Avg Gintropy | Expected Gini |
| ---------------------------------------- | --------------------------- | ---------- | -------------- | ------------ | ------------- |
| Regular (Communism)                      | 500                         | -          | 0              | 0            | 0             |
| Star network with n hubs (Communism++)\* | 404 (4 hubs and 100 leaves) | -          | 0.49748        | 0.49746      |               |
| Star network with n hubs (Communism++)\* | 84 (4 hubs and 20 leaves)   | -          | 0.4872         | 0.4866       |               |
| Star network with n hubs (Communism++)\* | 16 (4 hubs and 3 leaves)    | -          | 0.4166         | 0.3999       | 0.375         |
| ER (Natural)                             | 500                         | p = 0.1    | 0.0748         | 0.0521       | 0.5           |
| ER (Natural)                             | 500                         | p = 0.4    | 0.0307         | 0.0208       | 0.5           |
| Random degree sequence (Eco-window)      | 500                         | a=1, b=10  | 0.3007         | 0.2270       | <= 0.333      |
| Random degree sequence (Eco-window)      | 500                         | a=5, b=10  | 0.1294         | 0.0989       | <= 0.333      |
| Random degree sequence (Eco-window)      | 500                         | a=5, b=100 | 0.3028         | 0.2260       | <= 0.333      |
| BA (Capitalism)                          | 500                         | m=5        | 0.3486         | 0.2642       | >=0.5         |
| BA (Capitalism)                          | 500                         | m=10       | 0.3239         | 0.2452       | >=0.5         |
| BA (Capitalism)                          | 500                         | m=2        | 0.3850         | 0.2958       | >=0.5         |
| Star Graph                               | 500                         | -          | 0.4980         | 0.498        | 1             |
| Path Graph                               | 500                         | -          | 0.00199        | 0.0          | ?             |
| WS Graph                                 | 500                         | K=2, p=0.1 | 0.0823         | 0.0449       | ?             |
| WS Graph                                 | 500                         | K=4, p=0.1 | 0.0704         | 0.0408       | ?             |
| WS Graph                                 | 500                         | K=2, p=0.2 | 0.1392         | 0.0817       | ?             |
| WS Graph                                 | 500                         | K=2, p=0.4 | 0.2064         | 0.1335       | ?             |
| WS Graph                                 | 500                         | K=4, p=0.4 | 0.1524         | 0.1033       | ?             |
| Complete graph                           | 500                         | -          | 0.0            | 0.0          | 0             |

| Network                                  | Network Size                | Properties | Avg H Index | Avg Gintropy | Expected H |
| ---------------------------------------- | --------------------------- | ---------- | ----------- | ------------ | ---------- |
| Regular (Communism)                      | 500                         | -          | 0.0         | 0            | 0          |
| Star network with n hubs (Communism++)\* | 404 (4 hubs and 100 leaves) | -          | 0.49748     | 0.49746      | 0.4950     |
| Star network with n hubs (Communism++)\* | 84 (4 hubs and 20 leaves)   | -          | 0.48726     | 0.4866       | 0.4761     |
| Star network with n hubs (Communism++)\* | 16 (4 hubs and 3 leaves)    | -          | 0.416666    | 0.3999       | 0.375      |
| ER (Natural)                             | 500                         | p = 0.1    | 0.07572     | 0.0521       | 0.002236   |
| ER (Natural)                             | 500                         | p = 0.4    | 0.03084     | 0.0208       | 0.001118   |
| Random degree sequence (Eco-window)      | 500                         | a=1, b=10  | 0.29855     | 0.2270       |            |
| Random degree sequence (Eco-window)      | 500                         | a=5, b=10  | 0.12907     | 0.0989       |            |
| Random degree sequence (Eco-window)      | 500                         | a=5, b=100 | 0.30403     | 0.2260       |            |
| BA (Capitalism)                          | 500                         | m=5        | 0.34872     | 0.2642       |            |
| BA (Capitalism)                          | 500                         | m=10       | 0.32417     | 0.2452       |            |
| BA (Capitalism)                          | 500                         | m=2        | 0.38574     | 0.2958       |            |
| Star Graph                               | 500                         | -          | 0.49900000  | 0.498        | 0.5        |
| Path Graph                               | 500                         | -          | 0.0         | 0.0          | ?          |
| WS Graph                                 | 500                         | K=2, p=0.1 | 0.08312     | 0.0449       | ?          |
| WS Graph                                 | 500                         | K=4, p=0.1 | 0.07109     | 0.0408       | 0.07       |
| WS Graph                                 | 500                         | K=2, p=0.2 | 0.13825     | 0.0817       | ?          |
| WS Graph                                 | 500                         | K=2, p=0.4 | 0.20674     | 0.1335       | ?          |
| WS Graph                                 | 500                         | K=4, p=0.4 | 0.1522      | 0.1033       | 0.15       |
| Complete graph                           | 500                         | -          | 0.0         | 0.0          | 0          |

\*The hubs create a complete graph

## Figures

|                                      Communism                                       |                             Natural                              |
| :----------------------------------------------------------------------------------: | :--------------------------------------------------------------: |
| <img src="F:\projects\Complex-Networks\figures\Figure_2_Communism_regular_lorenz_curve.png"> | <img src="F:\projects\Complex-Networks\figures\Figure_2_natural_er.png"> |

|                              Eco-window                               |                              Capitalism                               |
| :-------------------------------------------------------------------: | :-------------------------------------------------------------------: |
| <img src="F:\projects\Complex-Networks\figures\Figure_2_eco_window_1_10.png"> | <img src="F:\projects\Complex-Networks\figures\Figure_2_capitalismBA_m5.png"> |

[1]
Biró, T.S.; Néda, Z. Gintropy: Gini Index Based Generalization of Entropy. Entropy 2020, 22, 879. https://doi.org/10.3390/e22080879
