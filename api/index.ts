import { convertImageGrayscale, getBase64Image } from './src/image-handler';
import { callOpenAI } from './src/call-openapi';

await convertImageGrayscale();
const imageBase64 = await getBase64Image();
callOpenAI(imageBase64);
