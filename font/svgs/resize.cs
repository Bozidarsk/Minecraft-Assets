using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;

class main 
{
	static void Main(string[] args) 
	{
		string[] files = Directory.GetFiles(Directory.GetCurrentDirectory(), "*.svg");

		for (int i = 0; i < files.Length; i++) 
		{
			string content = File.ReadAllText(files[i]);
			string n = "";
			int index = -1;

			index = content.IndexOf("width=\"");
			content = content.Remove(index, "width=\"".Length);
			n = content[index].ToString();
			content = content.Remove(index, 1);
			content = content.Insert(index, "width=\"" + (int.Parse(args[0]) + int.Parse(n)).ToString());

			index = content.IndexOf("viewBox=\"0 0 ");
			content = content.Remove(index, "viewBox=\"0 0 ".Length);
			n = content[index].ToString();
			content = content.Remove(index, 1);
			content = content.Insert(index, "viewBox=\"0 0 " + (int.Parse(args[0]) + int.Parse(n)).ToString());

			File.WriteAllText(files[i], content);
		}
	}
}