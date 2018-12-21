﻿package DTO;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

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
		
		final int AMOUNT_IMAGE = 1000;
		
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
        
        // Compute vector histogram query image    
        Mat qImage = Imgcodecs.imread(url, Imgcodecs.CV_LOAD_IMAGE_COLOR);
        int rw_qImage = qImage.rows();
        int cl_qImage = qImage.cols();       
        int r, c;
        if (rw_qImage > cl_qImage) {

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
        		
        		int[] arrCountA = new int[arrSize];
        		Arrays.fill(arrCountA, 0);

        		for (int k = i * rw_qImage / r; k < i * rw_qImage / r + rw_qImage / r; k++) {
        			for (int l = j * cl_qImage / c; l < j * cl_qImage / c + cl_qImage / c; l++) {
        				
        				int vt = Algorithm.findLocationMin(qImage, k, l, arrMPEG);

		        		int sum = Algorithm.sumArrayInteger(arrCountA);
		                
		                double percentBin = 0;
		                double[] vHistBin = new double[arrSize];
		                
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
        	}
        }
        
        //Name of folders in database
        String[] arr = new String[] { "peoples", "beach", "castle", "bus", "dinosaur", "elephant", "flower", "horse", "mountain", "meal" };
	   	
        //Compute distance between pixel from image  
        double[] histData = new double[r * c * arrSize * AMOUNT_IMAGE];
 	   	int[] arrNameImage = new int[AMOUNT_IMAGE];
 	   
 	   	//Read file date vector histogram
	 	FileInputStream fs = null;
		try {
			fs = new FileInputStream("/UploadMultipleImagesEMD/dataHistEMD_Euclide_Bins_Hist.bin");
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		DataInputStream ds = new DataInputStream(fs);
		for (int i = 0; i < r * c * arrSize * AMOUNT_IMAGE; i++) {
			try {
				histData[i] = ds.readDouble();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		for (int i = 0; i < AMOUNT_IMAGE; i++) {
			arrNameImage[i] = i;
		}
		
		//Tính khoang cách
		double[] arrDis = new double[AMOUNT_IMAGE];
		Arrays.fill(arrDis, 0);

        double[] arr1 = new double[arrSize];
        double[] c1 = new double[arrSize];
        int dir = 0;
        for (int a = 0; a < AMOUNT_IMAGE; a++) {
        	List<double[]> lstHistImg = new ArrayList<double[]>();
        	for (int i = 0; i < r * c; i++) {            	
            	double[] arrHist = new double[arrSize];
            	for (int k = 0; k < arrSize; k++) {
        			arrHist[k] = histData[dir];
        			dir++;
        		}
            	lstHistImg.add(arrHist);
        	}
            for (int j = 0; j < lstHist_qImage.size(); j++) {
        		double percent = 0;
        		for (int k = 0; k < arrSize; k++) {
        			percent += lstHistImg.get(j)[k];
        		}
        		for (int k = 0; k < arrSize; k++) {
            		arr1[k] = lstHistImg.get(j)[k];
            	}
        		for (int k = 0; k < arrSize; k++) {
            		c1[k] = lstHist_qImage.get(j)[k];
            	}
        		
        		if (percent >= arrPercentEachHist[j]) {
            		arrDis[a] += Algorithm.transportationProblem(arr1, c1, arrMPEG, arrPercentEachHist[j]);
            	}
            	else {
            		arrDis[a] += Algorithm.transportationProblem(c1, arr1, arrMPEG, percent);
            	}
            }
        }
        
        for(int i = 0; i < AMOUNT_IMAGE - 1; i++) {
        	for (int j = i + 1; j < AMOUNT_IMAGE; j++) {
        		if (arrDis[j] < arrDis[i]) {
        			double t = arrDis[j];
        			arrDis[j] = arrDis[i];
        			arrDis[i] = t;
        			int t1 = arrNameImage[j];
        			arrNameImage[j] = arrNameImage[i];
        			arrNameImage[i] = t1;
        		}
        	}
        }

        //Compute 
       int ten = arrNameImage[0];
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
    	   
        //Get top 100
        for (int i = 0; i < 100; i++) {
        	if(dem -100 <= arrNameImage[i] && arrNameImage[i]<= dem)
        		tile++;
			String url = "DBCOREL" + "/" + arr[arrNameImage[i] / 100] + "/" + arrNameImage[i] + ".jpg";
			Image img = new Image();
			img.idImage = arrNameImage[i];
			img.urlImage = url;
			this.lst.lstImage.add(img);
        }
		return this.lst;
	}	
}
