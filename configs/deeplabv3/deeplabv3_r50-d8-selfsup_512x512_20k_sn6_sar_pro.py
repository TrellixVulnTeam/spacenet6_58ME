'''
Author: Shuailin Chen
Created Date: 2021-09-14
Last Modified: 2021-09-25
	content: 
'''

_base_ = [
    '../_base_/models/deeplabv3_r50-d8-selfsup.py',
    '../_base_/datasets/sn6_sar_pro.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_20k.py'
]
model = dict(
    decode_head=dict(num_classes=2), auxiliary_head=dict(num_classes=2))
