{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e8320e95",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# data = np.array(['a','b','c','d'])\n",
    "data = {'a': 0.0, 'b': 0.1, 'c': 0.2}\n",
    "s=pd.Series([5,3,2,8,6], index=['b','c','d','a','f'])\n",
    "\n",
    "print(s['b'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3ddcf313",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Name  Age Phone Number\n",
      "0   Zain   20   0123456789\n",
      "1   Amir   22   0123555885\n",
      "2  Farah   20   0123666885\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data = [['Zain',20,'0123456789'],['Amir',22,'0123555885'],['Farah',20,'0123666885']]\n",
    "df = pd.DataFrame(data, columns=['Name', 'Age', 'Phone Number'])\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3563c33f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Name  Age PhoneNumber\n",
      "0   Zain   20  0123456789\n",
      "1   Amir   22  0123555885\n",
      "2  Farah   20  0123666885\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data = {'Name': ['Zain', 'Amir', 'Farah'], 'Age': [20,22,20], 'PhoneNumber': ['0123456789','0123555885','0123666885']}\n",
    "df = pd.DataFrame(data)\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e95a44b",
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
