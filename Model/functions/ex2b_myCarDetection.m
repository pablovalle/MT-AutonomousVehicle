%% コンピュータビジョンデモ：前方車両の検出
I = imread('IMG_5959_2a.jpg');
figure; imshow(I);

%% 物体認識オブジェクトの定義、実行 [２行のMATLABコード]
%     顔認識用のトレーニングされたデータは内蔵
detector = vision.CascadeObjectDetector('carDetector_20151015Bb.xml');
faces = step(detector, I)

%% 検出された顔の位置に、四角い枠とテキストを追加
I2 = insertObjectAnnotation(I, 'rectangle', faces, [1:size(faces,1)], 'FontSize',24, 'LineWidth', 4);
imshow(I2);shg;

release(detector);

%% 
% Copyright 2015 The MathWorks, Inc.

