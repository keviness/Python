from tqdm import tqdm
import time

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    # 设置描述
    pbar.set_description("Processing %s" % char)
    time.sleep(1)