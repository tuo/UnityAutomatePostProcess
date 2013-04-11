#if UNITY_IPHONE

using UnityEngine;
using UnityEditor;
using UnityEditor.Callbacks;

using System;
using System.Diagnostics;

public class CustomPostprocessScript : MonoBehaviour
{

	//IMPORTANT!!!
	//100 is order , it means this one will execute after e.g 1 as default one is 1 
	//it means our script will run after all other scripts got run
	[PostProcessBuild(100)]
	public static void OnPostprocessBuild(BuildTarget target, string pathToBuildProject)
	{
        
		UnityEngine.Debug.Log("----Custome Script---Executing post process build phase."); 		
		string objCPath = Application.dataPath + "/ObjC";
		Process myCustomProcess = new Process();		
		myCustomProcess.StartInfo.FileName = "python";
        myCustomProcess.StartInfo.Arguments = string.Format("Assets/Editor/post_process.py \"{0}\" \"{1}\"", pathToBuildProject, objCPath);
        myCustomProcess.StartInfo.UseShellExecute = false;
        myCustomProcess.StartInfo.RedirectStandardOutput = false;
		myCustomProcess.Start(); 
		myCustomProcess.WaitForExit();
		UnityEngine.Debug.Log("----Custome Script--- Finished executing post process build phase.");  
		
       
	}
}

#endif
