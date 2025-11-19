import numpy as np
from pathlib import Path

# ====================================
brw_file =    
WIDTH    =                
HEIGHT   =                   
# ====================================

brw_path = Path(brw_file)
file_size = brw_path.stat().st_size
print(f"文件大小：{file_size} 字节")

header_size = file_size - (WIDTH * HEIGHT * 2)

if header_size < 0:
    raise ValueError("文件比预期还小，宽高设置错了！")

print(f"头大小：{header_size} 字节")

# 读取原始像素
with open(brw_path, 'rb') as f:
    f.seek(header_size)
    raw16 = np.fromfile(f, dtype=np.uint16, count=WIDTH*HEIGHT)

# 取出干净的 12bit 原始数据（低12位有效）
raw_data = (raw16 & 0x0FFF).reshape(HEIGHT, WIDTH).astype(np.float32)

print(f"成功！尺寸 {WIDTH}×{HEIGHT}")
print(f"最大值 {raw_data.max():.0f}   均值 {raw_data.mean():.1f}")
