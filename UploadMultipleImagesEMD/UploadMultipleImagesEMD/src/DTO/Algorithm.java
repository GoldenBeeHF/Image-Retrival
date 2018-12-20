package DTO;

import java.util.List;
public class Algorithm {
	/**
	 function distanceEuclide  compute distance between 2 pixel
	 */
	public static double distanceEuclide(double[] a, double[] b) {
		return Math.sqrt(Math.pow(a[0] - b[0], 2) + Math.pow(a[1] - b[1], 2) + Math.pow(a[2] - b[2], 2));
	}		
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
