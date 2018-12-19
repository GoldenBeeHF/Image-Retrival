package DTO;

import java.util.ArrayList;

import org.w3c.dom.Element;

import DTO.Image;
public class ListImage {
	ArrayList<Image> lstImage = new ArrayList<>();

	public ArrayList<Image> getLstImage() {
		return lstImage;
	}

	public void setLstImage(ArrayList<Image> lstImage) {
		this.lstImage = lstImage;
	}
	
	public ListImage() {
		super();
		this.lstImage = new ArrayList<>();
	}
	public void Insert(Element node) {
		Image I = new Image();
		
		I.setIdImage(Integer.parseInt(node.getElementsByTagName("id").item(0).getTextContent()));
		
		I.setUrlImage(node.getElementsByTagName("urlimage").item(0).getTextContent());
		this.lstImage.add(I);
	}
	public Image search(int id)
	{
		
		Image iImage = new Image();
		for( int i = 0 ; i< this.lstImage.size(); i++)
		{
			
			if(id == this.lstImage.get(i).idImage)
			{
				
				iImage = this.lstImage.get(i);
				break;
			}
		}
		return iImage;
		
	}
	
	
	
}