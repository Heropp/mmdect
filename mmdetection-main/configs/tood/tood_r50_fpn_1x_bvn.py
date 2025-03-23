_base_ ='tood_r50_fpn_1x_coco.py'

model = dict(
    bbox_head=dict(
        num_classes=2
    )

)
data_root = r'F:\objectdetection_script-master\objectdetection_script-master'
metainfo = {
    'classes': ('bengbian', ),
    ##    (220, 20, 60),
    #]
}
train_dataloader = dict(
    batch_size=4,
    num_workers=8,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file=r'mmdet-course\bvn1\annotations\train.json',
        data_prefix=dict(img=r'mmdet-course\bvn1\images')))
val_dataloader = dict(
    batch_size=4,
    num_workers=8,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file=r'mmdet-course\bvn1\annotations\val.json',
        data_prefix=dict(img=r'mmdet-course\bvn1\images')))
test_dataloader = dict(
    batch_size=4,
    num_workers=8,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file=r'mmdet-course\bvn1\annotations\test.json',
        data_prefix=dict(img=r'mmdet-course\bvn1\images')))
val_evaluator = dict(ann_file=data_root + r'.\mmdet-course\bvn1\annotations\val.json')
test_evaluator = dict(ann_file=data_root + r'.\mmdet-course\bvn1\annotations\test.json')
default_hooks = dict(logger=dict(type='LoggerHook', interval=10))
load_from='tood_r50_fpn_1x_coco_20211210_103425-20e20746.pth'
# nohup python tools/train.py configs/tood/tood_r50_fpn_1x_visdrone.py > tood-visdrone.log 2>&1 & tail -f tood-visdrone.log
# python tools/test.py configs/tood/tood_r50_fpn_1x_visdrone.py work_dirs/tood_r50_fpn_1x_visdrone/epoch_12.pth --show --show-dir test_save
# python tools/test.py configs/tood/tood_r50_fpn_1x_visdrone.py work_dirs/tood_r50_fpn_1x_visdrone/epoch_12.pth --tta 