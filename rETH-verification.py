from web3 import Web3

# 定义输入数据
potential_solution = '0x4957054895df7ece4da7ff94dab41e299b44f586abac81da9ecbc8f1b3324bfe'
currentChallenge = '0x7245544800000000000000000000000000000000000000000000000000000000'

# 计算哈希值
hashed_solution = Web3.solidity_keccak(['bytes32', 'bytes32'], [potential_solution, currentChallenge])


# 转换哈希值为十六进制字符串
hashed_solution_hex = Web3.to_hex(hashed_solution)


# 检查哈希值前缀
is_valid = hashed_solution_hex.startswith('0x77777')

# 打印验证结果
print(f"is_valid: {is_valid}")
