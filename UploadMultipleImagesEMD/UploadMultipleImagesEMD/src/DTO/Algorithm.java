package DTO;

import java.util.List;

import org.opencv.core.Mat;
public class Algorithm {
	
	
	public static int sumArrayInteger(int[] a) {
		int sum = 0;
		for (int i = 0; i < a.length; i++) {
        	sum += a[i]; 	
        }	
		return sum;
	}
	
	public static int findLocationMin(Mat qImage, int k, int l, List<double[]> arrMPEG) {
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
