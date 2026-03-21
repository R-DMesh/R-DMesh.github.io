# R-DMesh: Video-Guided 3D Animation via Rectified Dynamic Mesh Flow

<p align="center">
  <a href="https://r-dmesh.github.io">Project Page</a> |
  <a href="#">Paper (arXiv)</a> |
  <a href="#">Code</a> |
  <a href="#">Video</a>
</p>

## Abstract

Video-guided 3D animation holds immense potential for content creation, offering intuitive and precise control over dynamic assets. However, practical deployment faces a critical yet frequently overlooked hurdle: the pose misalignment dilemma. In real-world scenarios, the initial pose of a user-provided static mesh rarely aligns with the starting frame of a reference video. Naively forcing a mesh to follow a mismatched trajectory inevitably leads to severe geometric distortion or animation failure. To address this, we present Rectified Dynamic Mesh (R-DMesh), a unified framework designed to generate high-fidelity 4D meshes that are ``rectified'' to align with video context. Unlike standard motion transfer approaches, our method introduces a novel VAE that explicitly disentangles the input into a conditional base mesh, relative motion trajectories, and a crucial rectification jump offset. This offset is learned to automatically transform the arbitrary pose of the input mesh to match the video's initial state before animation begins. We process these components via a Triflow Attention mechanism, which leverages vertex-wise geometric features to modulate the three orthogonal flows, ensuring physical consistency and local rigidity during the rectification and animation process. For generation, we employ a Rectified Flow-based Diffusion Transformer conditioned on pre-trained video latents, effectively transferring rich spatio-temporal priors to the 3D domain. To support this task, we construct Video-RDMesh, a large-scale dataset of over 500k dynamic mesh sequences specifically curated to simulate pose misalignment. Extensive experiments demonstrate that R-DMesh not only solves the alignment problem but also enables robust downstream applications, including pose retargeting and holistic 4D generation.

## Overview

<p align="center">
  <video src="assets/teaser_mp4.mp4" autoplay loop muted playsinline width="100%"></video>
</p>

## Citation

If you find this work useful, please consider citing:

```bibtex
@article{rdmesh2026,
  title={R-DMesh: Video-Guided 3D Animation via Rectified Dynamic Mesh Flow},
  author={Zijie Wu, Lixin Xu, Puhua Jiang, Sicong Liu, Chunchao Guo, Xiang Bai},
  journal={},
  year={2026}
}
