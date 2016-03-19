package com.example.clay.first_task;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;

/**
 * Created by clay on 19.03.16.
 */
public class ListViewActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.list_layout);
        //resources
        String[] numbers = getResources().getStringArray(R.array.numbers);
        //find particular view
        ListView listView = (ListView) findViewById(R.id.listView);
        //use adapter
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, R.layout.list_item, R.id.textView, numbers);
        listView.setAdapter(adapter);

    }
}
