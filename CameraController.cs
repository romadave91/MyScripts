using UnityEngine;
using System.Collections;

public class CameraController : MonoBehaviour {

	public GameObject player; 						//reference to the gameobject -> player
	private Vector3 offset;							// to hold the offset value and can be handled using the script
	// Use this for initialization
	void Start () {
	
		offset = transform.position;				//set the camera's position as the offset position
	}
	
	// Update is called once per frame
	void LateUpdate () {							//use lateupdate for procedural animation
	
		transform.position = player.transform.position + offset;  						//for every frame, update the position
	}
}
