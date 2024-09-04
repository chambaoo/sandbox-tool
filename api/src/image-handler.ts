import * as path from 'path';
import sharp from 'sharp';
import * as fs from 'fs/promises';

export const convertImageGrayscale = async () => {
  const inputFilePath = path.join(__dirname, '../data/sample.jpeg');
  const outputFilePath = path.join(__dirname, '../data/sample-proceed.jpeg');

  // 画像をモノクロに変換
  const grayscaleBuffer = await sharp(inputFilePath)
    .grayscale() // モノクロに変換
    .toBuffer();

  // 処理後の画像を保存
  await fs.writeFile(outputFilePath, grayscaleBuffer);
};

export const getBase64Image = async () => {
  const inputFilePath = path.join(__dirname, '../data/sample-proceed.jpeg');

  // 画像を読み込み
  const image = await sharp(inputFilePath).toBuffer();

  // Base64にエンコード
  const imageBase64 = image.toString('base64');

  // モノクロ画像のBase64サイズを確認
  console.log('Image Base64 Size:', Buffer.byteLength(imageBase64, 'base64'));

  return imageBase64;
};
