_base_ = './fcos_hrnetv2p_w18_gn-head_4x4_1x_coco.py'
# learning policy
lr_config = dict(step=[16, 22])
runner = dict(max_epochs=24)
