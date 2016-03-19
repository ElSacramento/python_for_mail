package com.example.clay.first_task;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;

/**
 * Created by clay on 19.03.16.
 */
public class StartActivity extends Activity implements View.OnClickListener{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.frame_layout);

        new Thread(new Runnable() {

            @Override
            public void run() {
                try {
                    Thread.sleep(20);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                Intent secondView = new Intent(StartActivity.this, ListViewActivity.class);
                startActivity(secondView);
            }
        }).start();

//        Button button = (Button)findViewById(R.id.button);
//        button.setOnClickListener(StartActivity.this);

    }
    @Override
    public void onClick(View v) {
        Intent secondView = new Intent(this, ListViewActivity.class);
        startActivity(secondView);
    }



}
