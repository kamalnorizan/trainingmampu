{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "704c3efc",
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
   "id": "10d840ef",
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
   "id": "49319bf6",
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
   "execution_count": 24,
   "id": "475231d1",
   "metadata": {},
   "outputs": [
    {
     "ename": "OSError",
     "evalue": "[Errno 22] Invalid argument: 'D:\\trainingmampu\\\\data.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-24-6b903d535d5c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mdf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"D:\\trainingmampu\\data.csv\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, dialect, error_bad_lines, warn_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options)\u001b[0m\n\u001b[0;32m    608\u001b[0m     \u001b[0mkwds\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkwds_defaults\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    609\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 610\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    611\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    612\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    460\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    461\u001b[0m     \u001b[1;31m# Create the parser.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 462\u001b[1;33m     \u001b[0mparser\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mTextFileReader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    463\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    464\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mchunksize\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0miterator\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m    817\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"has_index_names\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"has_index_names\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    818\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 819\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_make_engine\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    820\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    821\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_make_engine\u001b[1;34m(self, engine)\u001b[0m\n\u001b[0;32m   1048\u001b[0m             )\n\u001b[0;32m   1049\u001b[0m         \u001b[1;31m# error: Too many arguments for \"ParserBase\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1050\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mmapping\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# type: ignore[call-arg]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1051\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1052\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_failover_to_python\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, src, **kwds)\u001b[0m\n\u001b[0;32m   1865\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1866\u001b[0m         \u001b[1;31m# open handles\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1867\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_open_handles\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msrc\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1868\u001b[0m         \u001b[1;32massert\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhandles\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1869\u001b[0m         \u001b[1;32mfor\u001b[0m \u001b[0mkey\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m\"storage_options\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"encoding\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"memory_map\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"compression\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers.py\u001b[0m in \u001b[0;36m_open_handles\u001b[1;34m(self, src, kwds)\u001b[0m\n\u001b[0;32m   1360\u001b[0m         \u001b[0mLet\u001b[0m \u001b[0mthe\u001b[0m \u001b[0mreaders\u001b[0m \u001b[0mopen\u001b[0m \u001b[0mIOHanldes\u001b[0m \u001b[0mafter\u001b[0m \u001b[0mthey\u001b[0m \u001b[0mare\u001b[0m \u001b[0mdone\u001b[0m \u001b[1;32mwith\u001b[0m \u001b[0mtheir\u001b[0m \u001b[0mpotential\u001b[0m \u001b[0mraises\u001b[0m\u001b[1;33m.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1361\u001b[0m         \"\"\"\n\u001b[1;32m-> 1362\u001b[1;33m         self.handles = get_handle(\n\u001b[0m\u001b[0;32m   1363\u001b[0m             \u001b[0msrc\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1364\u001b[0m             \u001b[1;34m\"r\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\common.py\u001b[0m in \u001b[0;36mget_handle\u001b[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[0;32m    640\u001b[0m                 \u001b[0merrors\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"replace\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    641\u001b[0m             \u001b[1;31m# Encoding\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 642\u001b[1;33m             handle = open(\n\u001b[0m\u001b[0;32m    643\u001b[0m                 \u001b[0mhandle\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    644\u001b[0m                 \u001b[0mioargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOSError\u001b[0m: [Errno 22] Invalid argument: 'D:\\trainingmampu\\\\data.csv'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(\"data.csv\")\n",
    "\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a33d1db",
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
