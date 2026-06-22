import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    'timestamp': pd.date_range('2026-06-22 08:00:00', periods=1000, freq='5s'),
    'src_ip': [f'192.168.1.{np.random.randint(1,255)}' for _ in range(1000)],
    'dst_port': np.random.choice([80, 443, 22, 3389, 4444, 9999], 1000),
    'packet_size': np.random.normal(500, 100, 1000).astype(int),
    'bytes_out': np.random.normal(1000, 300, 1000).astype(int),
})
# Inject anomalies
df.loc[950:960, 'dst_port'] = 4444
df.loc[970:980, 'packet_size'] = 2500
df.to_csv('sample_network_logs.csv', index=False)
print("✅ sample_network_logs.csv created!")