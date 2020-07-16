//
//  ViewController.swift
//  The Night Porter
//
//  Created by Evert Ball on 7/15/20.
//  Copyright © 2020 Evert. All rights reserved.
//

// Here, we lnk all the "stuff" Apple have provided to support
// building a typical iOS application.
// (And not just the user interface "stuff", but infrastructure as well)
import UIKit

class ViewController: UIViewController {

    @IBAction func enableDarkMode(_ sender: Any) {
        view.backgroundColor = UIColor.darkGray
        
        // TODO: Change the text color of every label
        
        // get everything contained in the top-level view
        let everything = view.subviews
        
        for eachView in everything {
            // is it a label?
            if eachView is UILabel {
                // downcast as UILabel
                let currentLabel = eachView as! UILabel
                currentLabel.textColor = UIColor.lightGray
            }
        }
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }


}

