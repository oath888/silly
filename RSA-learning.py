from cryptography.hazmat.primitives import serialization

with open("C:/id_rsa", "rb") as f:
    private_key = serialization.load_ssh_private_key(
        f.read(),
        password=None,  # 若无密码则填 None
    )
# 提取 RSA 参数
numbers = private_key.private_numbers()
print(f'p: {numbers.p}\nq:{numbers.q}\nd:{numbers.d}\ndmp1: {numbers.dmp1}\n'
      f'dmq1: {numbers.dmq1}\niqmp: {numbers.iqmp}\n'
      f'public_numbers: {numbers.public_numbers}\n')

# from cryptography.hazmat.primitives import serialization

# with open("id_rsa", "rb") as f:
#     private_key = serialization.load_pem_private_key(  # 改用 PEM 加载函数
#         f.read(),
#         password=None,  # 如果密钥未加密
#     )
# numbers = private_key.private_numbers()
# print(numbers.p)
