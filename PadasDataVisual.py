{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c55563ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a1755022",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a5d5ca52",
   "metadata": {},
   "outputs": [],
   "source": [
    "from numpy.random import randn, randint, uniform, sample"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c7eeae75",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(randn(1000), index = pd.date_range('2021-01-01', periods = 1000), columns=['value'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ae73e1a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.762320</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>-0.291329</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-1.242510</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.144855</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>0.976869</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2023-09-23</th>\n",
       "      <td>-0.045123</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2023-09-24</th>\n",
       "      <td>-0.378979</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2023-09-25</th>\n",
       "      <td>0.860110</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2023-09-26</th>\n",
       "      <td>-0.499546</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2023-09-27</th>\n",
       "      <td>0.371000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               value\n",
       "2021-01-01  0.762320\n",
       "2021-01-02 -0.291329\n",
       "2021-01-03 -1.242510\n",
       "2021-01-04  0.144855\n",
       "2021-01-05  0.976869\n",
       "...              ...\n",
       "2023-09-23 -0.045123\n",
       "2023-09-24 -0.378979\n",
       "2023-09-25  0.860110\n",
       "2023-09-26 -0.499546\n",
       "2023-09-27  0.371000\n",
       "\n",
       "[1000 rows x 1 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b08ac3f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "ts = pd.Series(randn(1000), pd.date_range('2021-01-01', periods = 1000))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c5701786",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2021-01-01    0.975692\n",
       "2021-01-02    0.193501\n",
       "2021-01-03    1.502287\n",
       "2021-01-04   -0.390225\n",
       "2021-01-05    0.773782\n",
       "                ...   \n",
       "2023-09-23    1.303540\n",
       "2023-09-24    0.038236\n",
       "2023-09-25   -0.628242\n",
       "2023-09-26    0.119552\n",
       "2023-09-27   -0.279946\n",
       "Freq: D, Length: 1000, dtype: float64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "22673a2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ts.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c809e012",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2021-01-01     0.975692\n",
       "2021-01-02     1.169193\n",
       "2021-01-03     2.671480\n",
       "2021-01-04     2.281255\n",
       "2021-01-05     3.055037\n",
       "                ...    \n",
       "2023-09-23   -25.375269\n",
       "2023-09-24   -25.337033\n",
       "2023-09-25   -25.965276\n",
       "2023-09-26   -25.845724\n",
       "2023-09-27   -26.125670\n",
       "Freq: D, Length: 1000, dtype: float64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ts = ts.cumsum()\n",
    "ts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f183a311",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ts.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8075a46d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
