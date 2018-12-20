package com.codeFactory;

import java.io.File;
import java.io.IOException;

import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;

import DTO.test;


/**
 * Servlet implementation class UploadServlet
 */
@WebServlet("/UploadServlet")
public class UploadServlet extends HttpServlet {
	private final String UPLOAD_DIRECTORY = "/UploadMultipleImagesEMD/WebContent/Data";
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public UploadServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doPost(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	test computTest;
	@SuppressWarnings({ "static-access", "null", "unchecked" })
protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		if(ServletFileUpload.isMultipartContent(request)){
			try{
				List<FileItem> multiparts = new ServletFileUpload(new DiskFileItemFactory()).parseRequest(request);
				for(FileItem item : multiparts){
					if(!item.isFormField()){
						String name = new File(item.getName()).getName();
						String url = UPLOAD_DIRECTORY + File.separator + name;
						item.write(new File(url));
						computTest = new test(url);
					}
				}
				request.setAttribute("listImage",t.getImage());
				request.setAttribute("tile",t.tile);
			}
			catch(Exception ex){
				request.setAttribute("message", "File upload failed due to : " + ex);
			}
		}
		else
			request.setAttribute("message", "Sorry this servlet only handles file upload request.");
		request.getRequestDispatcher("/result.jsp").forward(request, response);
	}

}
