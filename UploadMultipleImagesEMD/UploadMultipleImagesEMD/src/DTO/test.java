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
		System.load("E:\\opencv\\build\\java\\x64\\" + Core.NATIVE_LIBRARY_NAME + ".dll");
		
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
        
        // Tính histogram ?nh truy?n vào
       
        Mat qImage = Imgcodecs.imread(url, Imgcodecs.CV_LOAD_IMAGE_COLOR);
        int rw_qImage = qImage.rows();
        int cl_qImage = qImage.cols();       
        int r, c;
        if (rw_qImage > cl_qImage) {
        	r = 12;
        	c = 8;
        }
        else {
        	r = 8;
        	c = 12;
        }
        
        List<double[]> lstHist_qImage = new ArrayList<double[]>();
        double[] arrPercentEachHist = new double[r * c];
        
        for (int i = 0; i < r; i++) {
        	for (int j = 0; j < c; j++) {        		
        		int[] arrCountA = new int[25];
		        for (int m = 0; m < 25; m++) {
		        	arrCountA[m] = 0;
		        }
		        
        		for (int k = i * rw_qImage / r; k < i * rw_qImage / r + rw_qImage / r; k++) {
        			for (int l = j * cl_qImage / c; l < j * cl_qImage / c + cl_qImage / c; l++) {
        				
        				int vt = findLocationMin(qImage, k, l, arrMPEG);
                		arrCountA[vt]++; 		
        			}
        		}
        		
        		int sum = sumArrayInteger(arrCountA);
                
                double percentBin = 0;
                double[] vHistBin = new double[25];
                
                for (int a = 0; a < 25; a++) {
                	vHistBin[a] = (double)arrCountA[a] / sum * 100;
                	if (vHistBin[a] < 10) {
                		vHistBin[a] = 0;
                	}
                	percentBin += vHistBin[a];
                }
                lstHist_qImage.add(vHistBin);
                arrPercentEachHist[i * c + j % c] = percentBin;
        	}
        }	
        
        String[] arr = new String[] { "peoples", "beach", "castle", "bus", "dinosaur", "elephant", "flower", "horse", "mountain", "meal" };
	   	
        //Tính kho?ng cách gi?a ?nh truy?n vào v?i các ?nh trong b? d? li?u  
        double[] histNum = new double[96 * 25 * 1000];
 	   	int[] tenAnh = new int[1000];
 	   
 	   	//Ð?c file histogram c?a b? ?nh
	 	FileInputStream fs = null;
		try {
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
			tenAnh[i] = i;
		}
		
		//Tính kho?ng cách
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
            		arrDis[a] += transportationProblem(arr1, c1, arrMPEG, arrPercent[j]);
            	}
            	else {
            		arrDis[a] += transportationProblem(c1, arr1, arrMPEG, percent);
            	}
            }
        }
        
        for(int i = 0; i < 1000 - 1; i++) {
        	for (int j = i + 1; j < 1000; j++) {
        		if (arrDis[j] < arrDis[i]) {
        			double t = arrDis[j];
        			arrDis[j] = arrDis[i];
        			arrDis[i] = t;
        			int t1 = tenAnh[j];
        			tenAnh[j] = tenAnh[i];
        			tenAnh[i] = t1;
        		}
        	}
        }

        // ?nh g?c
       int ten = tenAnh[0];
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
        	if(dem -100 <=tenAnh[i] && tenAnh[i]<= dem)
        		tile++;
			String url = "DBCOREL" + "/" + arr[tenAnh[i] / 100] + "/" + tenAnh[i] + ".jpg";
			Image img = new Image();
			img.idImage = tenAnh[i];
			img.urlImage = url;
			System.out.println(url);
			this.lst.lstImage.add(img);
        }
		return this.lst;
	}
	
	private static int sumArrayInteger(int[] a) {
		int sum = 0;
		for (int i = 0; i < a.length; i++) {
        	sum += a[i]; 	
        }	
		return sum;
	}
	
	private static int findLocationMin(Mat qImage, int k, int l, List<double[]> arrMPEG) {
		int arrSize = arrMPEG.size();
		double minimum = distanceEuclide(qImage.get(k, l), arrMPEG.get(0));	
		int vt = 0;
		
		for (int i = 1; i < arrSize; i++) {
			if (minimum > distanceEuclide(qImage.get(k, l), arrMPEG.get(i))) {
				minimum = distanceEuclide(qImage.get(k, l), arrMPEG.get(i));
				vt = i;
			}
		}
		return vt;
	}
	
	/**
	 * compute distance between 2 colors
	 * @param colorA : color A
	 * @param colorB : color B
	 * @return distance between color A and B.
	 */
	public static double distanceEuclide(double[] colorA, double[] colorB) {
		return Math.sqrt(Math.pow(colorA[0] - colorB[0], 2) + Math.pow(colorA[1] - colorB[1], 2) + Math.pow(colorA[2] - colorB[2], 2));
	}	
	
	/**
	 * compute distance between 2 vectors
	 * @param a : vector histogram A
	 * @param b : vector histogram B
	 * @param MPEG7 : list color MPEG-7
	 * @param percent : percent color of vector histogram A
	 * @return distance between vector A and B
	 */
	public static double transportationProblem(double[] a, double[] b, List<double[]> MPEG7, double percent) {
		double dis = 0;
		int vt = 0;
		for (int i = 0; i < a.length; i++) {
			if (vt == 25) 
				break;

			for (int j = vt; j < b.length; j++) {
				if (a[i] == 0) {
					vt = j;
					break;
				}
				if (b[vt] == 0) {
					vt = j + 1;
					if (vt == 25) {
						break;
					}
					continue;
				}
				
				if (a[i] >= b[j]) {
					dis += b[j] * distanceEuclide(MPEG7.get(i), MPEG7.get(j));
					a[i] -= b[j];
					b[j] = 0;
				}
				else {
					dis += a[i] * distanceEuclide(MPEG7.get(i), MPEG7.get(j));
					b[j] -= a[i];
					a[i] = 0;
					break;
				}
				
			}	
		}
		return dis / percent;
	}
}
