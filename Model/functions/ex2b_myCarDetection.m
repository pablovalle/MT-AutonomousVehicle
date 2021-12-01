%% �R���s���[�^�r�W�����f���F�O���ԗ��̌��o
I = imread('IMG_5959_2a.jpg');
figure; imshow(I);

%% ���̔F���I�u�W�F�N�g�̒�`�A���s [�Q�s��MATLAB�R�[�h]
%     ��F���p�̃g���[�j���O���ꂽ�f�[�^�͓���
detector = vision.CascadeObjectDetector('carDetector_20151015Bb.xml');
faces = step(detector, I)

%% ���o���ꂽ��̈ʒu�ɁA�l�p���g�ƃe�L�X�g��ǉ�
I2 = insertObjectAnnotation(I, 'rectangle', faces, [1:size(faces,1)], 'FontSize',24, 'LineWidth', 4);
imshow(I2);shg;

release(detector);

%% 
% Copyright 2015 The MathWorks, Inc.

