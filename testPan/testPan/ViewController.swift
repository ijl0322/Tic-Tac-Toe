//
//  ViewController.swift
//  testPan
//
//  Created by Isabel  Lee on 07/02/2017.
//  Copyright © 2017 Isabel  Lee. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var myX: UIImageView!
    
    @IBOutlet weak var centerblock: UIView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        // Create a pan gesture recoginzer
        let panGesture = UIPanGestureRecognizer(target: self, action: #selector(handlePan(_:)))
        
        // Add a tap gesture recognizer to the box
        myX.addGestureRecognizer(panGesture)
    }


    



// MARK: - Gesture Recognizers

/// Reposition the center of a view to correspond with a touch point
/// - Parameter recognizer: The gesture that is recognized
func handlePan(_ recognizer:UIPanGestureRecognizer) {
    
    // Determine where the view is in relation to the superview
    let translation = recognizer.translation(in: self.view)
    print("pan egsture")
    
    if let view = recognizer.view {
        // Set the view's center to the new position
        view.center = CGPoint(x:view.center.x + translation.x,
                              y:view.center.y + translation.y)
    }
    
    // Reset the translation back to zero, so we are dealing
    // in offsets
    recognizer.setTranslation(CGPoint.zero, in: self.view)
    
    if recognizer.state == UIGestureRecognizerState.ended {
        print("state ended")
        if (recognizer.view?.frame)!.intersects(self.centerblock.frame) {
            if let view = recognizer.view {
                // Set the view's center to the new position
                view.center = CGPoint(x: self.centerblock.center.x, y: self.centerblock.center.y)
            }
            
        }
    }
    
    

    
    
}


}

