# Lo que pretendo con este docker es que este limitado en memoria de la GPU
- Asi que le asignaremos este comando a la terminal general
sudo docker run \
    --rm \
    --gpus all \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    -e CUDA_DEVICE_MEMORY_LIMIT="4052MiB" \
    nvidia/cuda:12.1.1-base-ubuntu22.04 \
    nvidia-smi