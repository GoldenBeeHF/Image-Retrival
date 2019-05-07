package com.example.REST.service;

import java.util.ArrayList;
import java.util.List;

import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;
import org.springframework.stereotype.Repository;

import com.example.REST.model.Vector;


@Repository
public class VectorService {
	
	public List<Double> getResultVector(String url) {
		
		return mathVec(url);
	}
	
	private List<Double> mathVec(String url) {
		nu.pattern.OpenCV.loadShared();
		List<double[]> arrMPEG = new ArrayList<>();
		arrMPEG.add(new double[] { 0, 0, 0 }); // Black
		arrMPEG.add(new double[] { 0, 182, 0 }); // Sea Green
		arrMPEG.add(new double[] { 170, 255, 0 }); // Light Green
		arrMPEG.add(new double[] { 0, 73, 36 }); // Olive Green
		arrMPEG.add(new double[] { 170, 146, 36 }); // Aqua
		arrMPEG.add(new double[] { 0, 255, 36 }); // Bright Green
		arrMPEG.add(new double[] { 170, 36, 73 }); // Blue
		arrMPEG.add(new double[] { 0, 146, 73 }); // Green
		arrMPEG.add(new double[] { 170, 219, 73 }); // Turquoise
		arrMPEG.add(new double[] { 0, 36, 109 }); // Brown
		arrMPEG.add(new double[] { 170, 109, 109 }); // Blue Gray
		arrMPEG.add(new double[] { 0, 219, 109 }); // Lime
		arrMPEG.add(new double[] { 170, 0, 146 }); // Lavender
		arrMPEG.add(new double[] { 0, 109, 146 }); // Plum
		arrMPEG.add(new double[] { 170, 182, 146 }); // Teal
		arrMPEG.add(new double[] { 0, 0, 182 }); // Dark Red
		arrMPEG.add(new double[] { 170, 73, 182 }); // Magenta
		arrMPEG.add(new double[] { 0, 182, 182 }); // Yellow Green
		arrMPEG.add(new double[] { 170, 255, 182 }); // Flouro Green
		arrMPEG.add(new double[] { 0, 73, 219 }); // Red
		arrMPEG.add(new double[] { 170, 146, 219 }); // Rose
		arrMPEG.add(new double[] { 0, 255, 219 }); // Yellow
		arrMPEG.add(new double[] { 170, 36, 255 }); // Pink
		arrMPEG.add(new double[] { 0, 146, 255 }); // Orange
		arrMPEG.add(new double[] { 255, 255, 255 }); // White
		int arrSize = arrMPEG.size();

		// Tính histogram ?nh truy?n vào

		Mat anh = Imgcodecs.imread(url, Imgcodecs.CV_LOAD_IMAGE_COLOR);

		int[] arrCount = new int[25];
		for (int i = 0; i < 25; i++) {
			arrCount[i] = 0;
		}

		int rw = anh.rows();
		int cl = anh.cols();

		for (int i = 0; i < rw; i++) {
			for (int j = 0; j < cl; j++) {
				double minimum = distanceEuclide(anh.get(i, j), arrMPEG.get(0));

				int vt = 0;
				for (int k = 1; k < arrSize; k++) {
					if (minimum > distanceEuclide(anh.get(i, j), arrMPEG.get(k))) {
						minimum = distanceEuclide(anh.get(i, j), arrMPEG.get(k));
						vt = k;
					}
				}

				arrCount[vt]++;
			}
		}

		int sum = 0;

		for (int n = 0; n < 25; n++) {
			sum += arrCount[n];
		}

//		for (int i = 0; i < arrCount.length; i++) {
//			System.out.print(arrCount[i] + " ");
//		}

//		double[] vHist = new double[25];
		List<Double> vHist = new ArrayList<Double>();
		for (int i = 0; i < 25; i++) {
			vHist.add((double) arrCount[i] / sum);
		}
		return vHist;
	}
	public static double distanceEuclide(double[] a, double[] b) {
		return Math.sqrt(Math.pow(a[0] - b[0], 2) + Math.pow(a[1] - b[1], 2) + Math.pow(a[2] - b[2], 2));
	}
}
