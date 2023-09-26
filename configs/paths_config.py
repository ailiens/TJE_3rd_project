dataset_paths = {
    'celeba_test': 'D:\\face_image_data\\valid\\image\\',
    # 'celeba_test': '/content/drive/MyDrive/3차프로젝트/data/data_ex_class/training/images/00~09',
    'ffhq': 'D:\\face_image_data\\train\\image\\',
    # 'ffhq': '/content/drive/MyDrive/3차프로젝트/data/data_ex_class/training/images/10~19'
}

model_paths = {
    # 'pretrained_psp_encoder': 'pretrained_models/psp_ffhq_encode.pt',
    'pretrained_psp': 'pretrained_models/psp_ffhq_encode.pt',
    'ir_se50': '../pretrained_models/model_ir_se50.pth',
    'stylegan_ffhq': '../pretrained_models/stylegan2-ffhq-config-f.pt',
    'shape_predictor': 'shape_predictor_68_face_landmarks.dat',
    'age_predictor': '../pretrained_models/dex_age_classifier.pth',
}
