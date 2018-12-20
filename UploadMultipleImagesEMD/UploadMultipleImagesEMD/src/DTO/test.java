package DTO;
import java.util.List;
import java.util.ArrayList;
import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import DTO.ListImage;
import DTO.Image;
import DTO.Algorithm;
public class test {
	String url;
	public String getUrl() {
		return url;
	}

	public void setUrl(String url) {
		this.url = url;
	}
	public test(String url)
	{
		this.url = url;
	}
	public int tile = 0;
	int dem;
	ListImage lst = new ListImage();
	public  ListImage getImage() throws IOException{ 
		System.load("F:\\OpenCV\\opencv\\build\\java\\x64\\" + Core.NATIVE_LIBRARY_NAME + ".dll");
		
		List<double[]> arrMPEG = new ArrayList<>();
	       
        arrMPEG.add(new double[] {0, 0, 0}); //Black
        arrMPEG.add(new double[] {0, 182, 0}); //Sea Green
        arrMPEG.add(new double[] {170, 255, 0}); //Light Green
        arrMPEG.add(new double[] {0, 73, 36}); //Olive Green
        arrMPEG.add(new double[] {170, 146, 36}); //Aqua
        arrMPEG.add(new double[] {0, 255, 36}); //Bright Green
        arrMPEG.add(new double[] {170, 36, 73}); //Blue
        arrMPEG.add(new double[] {0, 146, 73}); //Green
        arrMPEG.add(new double[] {170, 219, 73}); //Turquoise
        arrMPEG.add(new double[] {0, 36, 109}); //Brown
        arrMPEG.add(new double[] {170, 109, 109}); //Blue Gray
        arrMPEG.add(new double[] {0, 219, 109}); //Lime
        arrMPEG.add(new double[] {170, 0, 146}); //Lavender
        arrMPEG.add(new double[] {0, 109, 146}); //Plum
        arrMPEG.add(new double[] {170, 182, 146}); //Teal
        arrMPEG.add(new double[] {0, 0, 182}); //Dark Red
        arrMPEG.add(new double[] {170, 73, 182}); //Magenta
        arrMPEG.add(new double[] {0, 182, 182}); //Yellow Green
        arrMPEG.add(new double[] {170, 255, 182}); //Flouro Green
        arrMPEG.add(new double[] {0, 73, 219}); //Red
        arrMPEG.add(new double[] {170, 146, 219}); //Rose
        arrMPEG.add(new double[] {0, 255, 219}); //Yellow
        arrMPEG.add(new double[] {170, 36, 255}); //Pink
        arrMPEG.add(new double[] {0, 146, 255}); //Orange
        arrMPEG.add(new double[] {255, 255, 255}); //White
        int arrSize = arrMPEG.size();
        
     // Compute Histogram image trainmision

        Mat requery_Image = Imgcodecs.imread(url, Imgcodecs.CV_LOAD_IMAGE_COLOR);
        int rw_num = requery_Image.rows();
        int cl_num = requery_Image.cols();       
        int r, c;
        if (rw_num > cl_num) {
        	r = 12;
        	c = 8;
        }
        else {
        	r = 8;
        	c = 12;
        }
        
        List<double[]> lst = new ArrayList<double[]>();
        double[] arrPercent = new double[r * c];
        
        for (int i = 0; i < r; i++) {
        	for (int j = 0; j < c; j++) {        		
        		int[] arrCountA = new int[25];
		        for (int m = 0; m < 25; m++) {
		        	arrCountA[m] = 0;
		        }
		        
        		for (int k = i * rw / r; k < i * rw / r + rw / r; k++) {
        			for (int l = j * cl / c; l < j * cl / c + cl / c; l++) {
        				double minimum = Algorithm.distanceEuclide(requery_Image.get(k, l), arrMPEG.get(0));	
                		int vt = 0;
                		
                		for (int m = 1; m < arrSize; m++) {
                			if (minimum > Algorithm.distanceEuclide(requery_Image.get(k, l), arrMPEG.get(m))) {
                				minimum = Algorithm.distanceEuclide(requery_Image.get(k, l), arrMPEG.get(m));
                			
                				vt = m;
                			}
                		}
                		arrCountA[vt]++; 		
        			}
        		}
        		
        		int sum = 0;                
                for (int n = 0; n < 25; n++) {
                	sum += arrCountA[n]; 	
                }
                
                double percentImage1 = 0;
                double[] vHist = new double[25];
                
                for (int a = 0; a < 25; a++) {
                	vHist[a] = (double)arrCountA[a] / sum * 100;
                	if (vHist[a] < 10) {
                		vHist[a] = 0;
                	}
                	percentImage1 += vHist[a];
                }
                lst.add(vHist);
                arrPercent[i * c + j % c] = percentImage1;
        	}
        }	
        
        String[] arr = new String[] { "peoples", "beach", "castle", "bus", "dinosaur", "elephant", "flower", "horse", "mountain", "meal" };
	   	
        //Compute distance between pixel from image  
        double[] histNum = new double[96 * 25 * 1000];
 	   	int[] tenrequery_Image = new int[1000];
 	   
 	   	//Read file date vector Historgram
	 	FileInputStream fs = null;
		try {
// 			fs = new FileInputStream("F:\\Studio\\eclipse-workspace\\UploadMultipleImagesEMD\\UploadMultipleImagesEMD\\dataHistEMD_Euclide_Bins_Hist.bin");
// =======
			//fs = new FileInputStream("C:\\Users\\Dell7559\\eclipse-workspace\\UploadMultipleImagesEMD\\UploadMultipleImagesEMD\\dataHistEuclide.bin");
			fs = new FileInputStream("/UploadMultipleImagesEMD/dataHistEMD_Euclide_Bins_Hist.bin");
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		DataInputStream ds = new DataInputStream(fs);
		for (int i = 0; i < 96 * 25 * 1000; i++) {
			try {
				histNum[i] = ds.readDouble();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		for (int i = 0; i < 1000; i++) {
			tenrequery_Image[i] = i;
		}
		
		//Tính khoang cách
		double[] arrDis = new double[1000];
		for (int i = 0; i < arrDis.length; i++) {
			arrDis[i] = 0;
		}
        double[] arr1 = new double[25];
        double[] c1 = new double[25];
        int dir = 0;
        for (int a = 0; a < 1000; a++) {
        	List<double[]> lstImg = new ArrayList<double[]>();
        	for (int i = 0; i < 96; i++) {            	
            	double[] arrHist = new double[25];
            	for (int k = 0; k < 25; k++) {
        			arrHist[k] = histNum[dir];
        			dir++;
        		}
        		lstImg.add(arrHist);	
        	}
            for (int j = 0; j < lst.size(); j++) {
        		double percent = 0;
        		for (int k = 0; k < 25; k++) {
        			percent += lstImg.get(j)[k];
        		}
        		for (int k = 0; k < 25; k++) {
            		arr1[k] = lstImg.get(j)[k];
            	}
        		for (int k = 0; k < 25; k++) {
            		c1[k] = lst.get(j)[k];
            	}
        		
        		if (percent >= arrPercent[j]) {
            		arrDis[a] += Algorithm.transportationProblem(arr1, c1, arrMPEG, arrPercent[j]);
            	}
            	else {
            		arrDis[a] += Algorithm.transportationProblem(c1, arr1, arrMPEG, percent);
            	}
            }
        }
        
        for(int i = 0; i < 1000 - 1; i++) {
        	for (int j = i + 1; j < 1000; j++) {
        		if (arrDis[j] < arrDis[i]) {
        			double t = arrDis[j];
        			arrDis[j] = arrDis[i];
        			arrDis[i] = t;
        			int t1 = tenrequery_Image[j];
        			tenrequery_Image[j] = tenrequery_Image[i];
        			tenrequery_Image[i] = t1;
        		}
        	}
        }

        //Compute 
       int ten = tenrequery_Image[0];
       if(ten<101)
    	   dem = 101;
       else if(ten < 200)
    	   dem = 200;
       else if(ten < 300)
    	   dem = 300;
       else if(ten < 400)
    	   dem = 400;
       else if(ten < 500)
    	   dem = 500;
       else if(ten < 600)
    	   dem = 600;
       else if(ten < 700)
    	   dem = 700;
       else if(ten < 800)
    	   dem = 800;
       else if(ten < 900)
    	   dem = 900;
       else 
    	   dem = 1000;
    	   
        //Xu?t ?nh top 100
        for (int i = 0; i < 100; i++) {
        	if(dem -100 <=tenrequery_Image[i] && tenrequery_Image[i]<= dem)
        		tile++;
			String url = "DBCOREL" + "/" + arr[tenrequery_Image[i] / 100] + "/" + tenrequery_Image[i] + ".jpg";
			Image img = new Image();
			img.idImage = tenrequery_Image[i];
			img.urlImage = url;
			System.out.println(url);
			this.lst.lstImage.add(img);
        }
		return this.lst;
	}
	
	
//	public static double Algorithm.distanceEuclide(double[] a, double[] b) {
//		return Math.sqrt(Math.pow(a[0] - b[0], 2) + Math.pow(a[1] - b[1], 2) + Math.pow(a[2] - b[2], 2));
//	}	
	
//	public static double Algorithm.transportationProblem(double[] a, double[] b, List<double[]> MPEG7, double percent) {
//		double dis = 0;
//		int vt = 0;
//
////		for (int i = 0; i < a.length; i++) {
////			if (a[i] > b[i]) {
////				a[i] -= b[i];
////				b[i] = 0;
////			}
////			else if (a[i] < b[i]) {
////				b[i] -= a[i];
////				a[i] = 0;
////			}
////			else 
////				a[i] = b[i] = 0;
////		}
//	
//		for (int i = 0; i < a.length; i++) {
//			if (vt == 25) 
//				break;
//
//			for (int j = vt; j < b.length; j++) {
//				if (a[i] == 0) {
//					vt = j;
//					break;
//				}
//				if (b[vt] == 0) {
//					vt = j + 1;
//					if (vt == 25) {
//						break;
//					}
//					continue;
//				}
//				
//				if (a[i] >= b[j]) {
//					dis += b[j] * Algorithm.distanceEuclide(MPEG7.get(i), MPEG7.get(j));
//					a[i] -= b[j];
//					b[j] = 0;
//				}
//				else {
//					dis += a[i] * Algorithm.distanceEuclide(MPEG7.get(i), MPEG7.get(j));
//					b[j] -= a[i];
//					a[i] = 0;
//					break;
//				}
//				
//			}	
//		}
//		
////		double modulePercent = 0;
////		for (int i = 0; i < a.length; i++) {
////			modulePercent += a[i];
////		}
////		
////		return dis / percent + (modulePercent * 100);
//		return dis / percent;
//	}
}
