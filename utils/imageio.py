from .inference_mmdet import show_result
from .inference_mmpose import vis_pose_result
from .utils import check_case_len

import numpy as np
import os.path as osp


def draw_box_results(
    img, 
    det_results, 
    det_save_path,
    bbox_thr,
    only_person=True):
    img_name = osp.splitext(osp.basename(img))[0]
    vis_name = f'vis_det_{img_name}.png'
    out_file = osp.join(det_save_path, vis_name)

    show_result(img,
                det_results,
                score_thr=bbox_thr,
                wait_time=0,
                only_person=only_person,
                out_file=out_file)


def draw_pose_results_with_box(
    pose_model,
    img,
    pose_results,
    radius,
    thickness,
    kpt_score_thr,
    dataset,
    show,
    pose_save_path):
    img_name = osp.splitext(osp.basename(img))[0]
    vis_name = f'vis_pose_{img_name}.png'
    out_file = osp.join(pose_save_path, vis_name)

    vis_pose_result(
        pose_model,
        img,
        pose_results,
        radius=radius,
        thickness=thickness,
        dataset=dataset,
        kpt_score_thr=kpt_score_thr,
        show=show,
        out_file=out_file)


def draw_bottomup_pose_results(
    pose_model,
    img,
    pose_results,
    radius,
    thickness,
    dataset,
    kpt_score_thr,
    show,
    pose_save_path):
    img_name = osp.splitext(osp.basename(img))[0]
    vis_name = f'vis_pose_{img_name}.png'
    out_file = osp.join(pose_save_path, vis_name)

    vis_pose_result(
        pose_model,
        img,
        pose_results,
        radius=radius,
        thickness=thickness,
        dataset=dataset,
        kpt_score_thr=kpt_score_thr,
        show=show,
        out_file=out_file)