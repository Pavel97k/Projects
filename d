[33mcommit 4a388cac49c285ae34c33c5b3a5ac93658e6cd58[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m, [m[1;31morigin/master[m[33m)[m
Author: Pavel97k <75374738+Pavel97k@users.noreply.github.com>
Date:   Tue Jun 13 18:29:25 2023 +0300

    PR_Python

[1mdiff --git "a/\320\237\321\200\320\260\320\272\321\202\320\270\321\207\320\265\321\201\320\272\320\260\321\217 \321\200\320\260\320\261\320\276\321\202\320\260 1 - \320\240\320\260\320\267\320\262\320\265\320\264\320\276\321\207\320\275\321\213\320\271 \320\260\320\275\320\260\320\273\320\270\320\267/PR4.ipynb" "b/\320\237\321\200\320\260\320\272\321\202\320\270\321\207\320\265\321\201\320\272\320\260\321\217 \321\200\320\260\320\261\320\276\321\202\320\260 1 - \320\240\320\260\320\267\320\262\320\265\320\264\320\276\321\207\320\275\321\213\320\271 \320\260\320\275\320\260\320\273\320\270\320\267/PR4.ipynb"[m
[1mnew file mode 100644[m
[1mindex 0000000..136c6e8[m
[1m--- /dev/null[m
[1m+++ "b/\320\237\321\200\320\260\320\272\321\202\320\270\321\207\320\265\321\201\320\272\320\260\321\217 \321\200\320\260\320\261\320\276\321\202\320\260 1 - \320\240\320\260\320\267\320\262\320\265\320\264\320\276\321\207\320\275\321\213\320\271 \320\260\320\275\320\260\320\273\320\270\320\267/PR4.ipynb"[m	
[36m@@ -0,0 +1,1802 @@[m
[32m+[m[32m{[m
[32m+[m[32m "cells": [[m
[32m+[m[32m  {[m
[32m+[m[32m   "attachments": {},[m
[32m+[m[32m   "cell_type": "markdown",[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "source": [[m
[32m+[m[32m    "// импорт библиотек для работы с файлом csv"[m
[32m+[m[32m   ][m
[32m+[m[32m  },[m
[32m+[m[32m  {[m
[32m+[m[32m   "cell_type": "code",[m
[32m+[m[32m   "execution_count": 256,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [],[m
[32m+[m[32m   "source": [[m
[32m+[m[32m    "import pandas as pd\n",[m
[32m+[m[32m    "import numpy as np"[m
[32m+[m[32m   ][m
[32m+[m[32m  },[m
[32m+[m[32m  {[m
[32m+[m[32m   "attachments": {},[m
[32m+[m[32m   "cell_type": "markdown",[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "source": [[m
[32m+[m[32m    "// Запись в переменную файла и его чтение."[m
[32m+[m[32m   ][m
[32m+[m[32m  },[m
[32m+[m[32m  {[m
[32m+[m[32m   "cell_type": "code",[m
[32m+[m[32m   "execution_count": 257,[m
[32m+[m[32m   "metadata": {},[m
[32m+[m[32m   "outputs": [[m
[32m+[m[32m    {[m
[32m+[m[32m     "data": {[m
[32m+[m[32m      "text/html": [[m
[32m+[m[32m       "<div>\n",[m
[32m+[m[32m       "<style scoped>\n",[m
[32m+[m[32m       "    .dataframe tbody tr th:only-of-type {\n",[m
[32m+[m[32m       "        vertical-align: middle;\n",[m
[32m+[m[32m       "    }\n",[m
[32m+[m[32m       "\n",[m
[32m+[m[32m       "    .dataframe tbody tr th {\n",[m
[32m+[m[32m       "        vertical-align: top;\n",[m
[32m+[m[32m       "    }\n",[m
[32m+[m[32m       "\n",[m
[32m+[m[32m       "    .dataframe thead th {\n",[m
[32m+[m[32m       "        text-align: right;\n",[m
[32m+[m[32m       "    }\n",[m
[32m+[m[32m       "</style>\n",[m
[32m+[m[32m       "<table border=\"1\" class=\"dataframe\">\n",[m
[32m+[m[32m       "  <thead>\n",[m
[32m+[m[32m       "    <tr style=\"text-align: right;\">\n",[m
[32m+[m[32m       "      <th></th>\n",[m
[32m+[m[32m       "      <th>Rank</th>\n",[m
[32m+[m[32m       "      <th>Name</th>\n",[m
[32m+[m[32m       "      <th>Platform</th>\n",[m
[32m+[m[32m       "      <th>Year</th>\n",[m
[32m+[m[32m       "      <th>Genre</th>\n",[m
[32m+[m[32m       "      <th>Publisher</th>\n",[m
[32m+[m[32m       "      <th>NA_Sales</th>\n",[m
[32m+[m[32m       "      <th>EU_Sales</th>\n",[m
[32m+[m[32m       "      <th>JP_Sales</th>\n",[m
[32m+[m[32m       "      <th>Other_Sales</th>\n",[m
[32m+[m[32m       "      <th>Global_Sales</th>\n",[m
[32m+[m[32m       "    </tr>\n",[m
[32m+[m[32m       "  </thead>\n",[m
[32m+[m[32m       "  <tbody>\n",[m
[32m+[m[32m       "    <tr>\n",[m
[32m+[m[32m       "      <th>0</th>\n",[m
[32m+[m[32m       "      <td>15197</td>\n",[m
[32m+[m[32m       "      <td>Let's Play Flight Attendant</td>\n",[m
[32m+[m[32m       "      <td>DS</td>\n",[m
[32m+[m[32m       "      <td>2010.0</td>\n",[m
[32m+[m[32m       "      <td>Simulation</td>\n",[m
[32m+[m[32m       "      <td>Deep Silver</td>\n",[m
[32m+[m[32m       "      <td>0.02</td>\n",[m
[32m+[m[32m       "      <td>0.00</td>\n",[m
[32m+[m[32m       "      <td>0.0</td>\n",[m
[32m+[m[32m       "      <td>0.00</td>\n",[m
[32m+[m[32m       "      <td>0.02</td>\n",[m
[32m+[m[32m       "    </tr>\n",[m
[32m+[m[32m       "    <tr>\n",[m
[32m+[m[32m       "      <th>1</th>\n",[m
[32m+[m[32m       "      <td>5292</td>\n",[m
[32m+[m[32m       "      <td>Mini Ninjas</td>\n",[m
[32m+[m[32m       "      <td>DS</td>\n",[m
[32m+[m[32m       "      <td>2009.0</td>\n",[m
[32m+[m[32m       "      <td>Action</td>\n",[m
[32m+[m[32m       "      <td>Eidos Interactive</td>\n",[m
[32m+[m[32m       "      <td>0.17</td>\n",[m
[32m+[m[32m       "      <td>0.15</td>\n",[m
[32m+[m[32m       "      <td>0.0</td>\n",[m
[32m+[m[32m       "      <td>0.04</td>\n",[m
[32m+[m[32m       "      <td>0.35</td>\n",[m
[32m+[m[32m       "    </tr>\n",[m
[32m+[m[32m       "    <tr>\n",[m
[32m+[m[32m       "      <th>2</th>\n",[m
[32m+[m[32m       "      <td>3119</td>\n",[m
[32m+[m[32m       "      <td>SingStar Pop Hits</td>\n",[m
[32m+[m[32m       "      <td>PS2</td>\n",[m
[32m+[m[32m       "      <td>2007.0</td>\n",[m
[32m+[m[32m       "      <td>Misc</td>\n",[m
[32m+[m[32m       "      <td>Sony Computer Entertainment</td>\n",[m
[32m+[m[32m       "      <td>0.00</td>\n",[m
[32m+[m[32m       "      <td>0.50</td>\n",[m
[32m+[m[32m       "      <td>0.0</td>\n",[m
[32m+[m[32m       "      <td>0.15</td>\n",[m
[32m+[m[32m       "      <td>0.65</td>\n",[m
[32m+[m[32m       "    </tr>\n",[m
[32m+[m[32m       "    <tr>\n",[m
[32m+[m[32m       "      <th>3</th>\n",[m
[32m+[m[32m       "      <td>13923</td>\n",[m
[32m+[m[32m       "      <td>Super Army War</td>\n",[m
[32m+[m[32m       "      <td>GBA</td>\n",[m
[32m+[m[32m       "      <td>2005.0</td>\n",[m
[32m+[m[32m       "      <td>Action</td>\n",[m
[32m+[m[32m       "      <td>Flashpoint Games</td>\n",[m
[32m+[m[32m       "      <td>0.03</td>\n",[m
[32m+[m[32m       "      <td>0.01</td>\n",[m
[32m+[m[32m       "      <td>0.0</td>\n",[m
[32m+[m[32m       "      <td>0.00</td>\n",[m
[32m+[m[32m       "      <td>0.04</td>\n",[m
[32m+[m[32m       "    </tr>\n",[m
[32m+[m[32m       "    <tr>\n",[m
[32m+[m[32m       "      <th>4</th>\n",[m
[32m+[m[32m       "      <td>7564</td>\n",[m
[32m+[m[32m       "      <td>Rocket Power: Zero Gravity Zone</td>\n",[m
[32m+[m[32m       "      <td>GBA</td>\n",[m
[32m+[m[32m       "      <td>2003.0</td>\n",[m
[32m+[m[32m       "      <td>Sports</td>\n",[m
[32m+[m[32m       "      <td>THQ</td>\n",[m
[32m+[m[32m       "      <td>0.14</td>\n",[m
[32m+[m[32m       "      <td>0.05</td>\n",[m
[32m+[m[32m       "      <td>0.0</td>\n",[m
[32m+[m[32m       "      <td>0.00</td>\n",[m
[32m+[m[32m       "      <td>0.20</td>\n",[m
[32m+[m[32m       "    </tr>\n",[m
[32m+[m[32m       "    <tr>\n",[m
[32m+[m[32m       "      <th>...</th>\n",[m
[32m+[m[32m       "      <td>...</td>\n",[m
[32m+[m[32m       "      <td>...</td>\n",[m
[32m+[m[32m       "      <td>...</td>\n",[m
[32m+[m[32m       "      <td>...</td>\n",[m
[32m+[m[32m       "      <td>...</td>\n",[m
[32m+[m[32m       "      <td>...</td>\n",[m
[32m+[m[32m       "      <td>...</td>\n",[m
[32m+[m[32m       "      <td>...</td>\n",[m
[32m+[m[32m       "      <td>...</td>\n",[m
[32m+[m[32m       "      <td>...</td>\n",[m
[32m+[m[32m       "    