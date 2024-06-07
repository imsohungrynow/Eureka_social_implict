import torch
x = torch.rand(5, 3)
print(x)
print(torch.cuda.is_available())

print("PyTorch version: {}".format(torch.__version__))
print("CUDA version: {}".format(torch.version.cuda))