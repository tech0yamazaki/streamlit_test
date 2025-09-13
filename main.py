import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit Hello World') # タイトル

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
}) # データフレームの作成

st.write(df)  # データフレームの表示
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100) # データフレームの表示（スタイル付き）

#公式ドキュメントを見に行くと、いろんな表示形式があるので確認する（display data）

st.table(df.style.highlight_max(axis=0)) # データフレームの表示（スタイル付き）

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""