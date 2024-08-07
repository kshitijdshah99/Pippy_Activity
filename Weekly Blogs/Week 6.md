# Progress till Now📈
In the 5th week I had designed a rough figma design for the Pippy's new UI look. I had to talk about the same with the mentors. Main goal was to keep the UI consistent as much as possible with respect to all other Sugar-activities where chatbot was to be integrated. For an instance I tried keeping UI similar to that of Chat Activity which my co-mentor was making.

# Week 6
This week was spent in doing 3 tasks which where quite experimental and time consuming too. Since these formed the fundamental basis of Pippy's UI I tried to sort them out on priority basis.
1. Setting up Sugar
2. Exploring the Pippy repository
3. Making a roadmap so as how to develop UI.

This is just what I had planned I was yet to decide and communicate with the mentors about the plan.

## Setting up Sugar
Instead of doing dual boot I preferred using a Virtual Machine as it gives us more flexibility to work with the desktop environment. However this task consumed most of my time this week.
### Issues I had encountered⚠
I had previously setup Sugar using live-build on debain and packed sugar on ubuntu, however I had faced many challenges like RAM allocation, not possible to maximize full screen, lot of lag in opening Sugar activities which made it difficult for me to contribute to the desktop environment. 

### Solution😊
To overcome this problem I once again started setting-up packed sugar on a virtual machine having Ubuntu on it. I had allocated 100GB of space to it hence there was minimal lag this time. Once Ubuntu was setup I did following steps.

**1. Installed Packed-sugar using help of this [documentation](https://github.com/sugarlabs/sugar/blob/master/docs/development-environment.md)**
 
**2. Downloaded dev tools like VS code**

**3. And started installing other tools like Zephyr**

**4. Increasing the size of Ubuntu screen** - This issue personally took a lot of time to get sorted. If like me anyone is facing any issues with this I recommend to watch this [video](https://youtu.be/w4E1iqsn_wA?si=P60lWiJbKu9-9FY8).

For those who read my articles, I found [this video](https://www.youtube.com/watch?v=x5MhydijWmc&pp=ygUbc2V0dGluZyB1cCB0aGUgdm0gb2YgdWJ1bnR1) to be quite useful for installing Ubuntu on a virtual machine, you can surely refer for the same.

## Exploring the [Pippy Repository](https://github.com/sugarlabs/Pippy)👨‍💻
This was quite challenging because I was not familiar with the Pippy's codebase. I had asked mentors for a personal meet if I was unable to sort out things well. 
The repository was quite big having many code files making it complex to understand.

To simplify it i first sorted out all the files which seemed redundant to me as far as UI was concerned. Like 
Next step I dived into code of the remaining files understanding what the functions performed and what were these class made of. This helped me understand good amount of sugar codebase.
After this I looked what exactly the GTK functions performed in those code and tried to figure out rough analogy between the UI and codebase.

I have understood codebase to quite a good extent till now, if I am unable to figure out things by next week I will surely approach the mentors.

## Road map for developing UI of Pippy🐍

### Figma Design-1
![](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Output/User%20Interface/FIGMA%20DESIGN-1.gif)

In this design I would be basically following this steps

**Step 1.** Choose an icon for the AI-assistant and choose a suitable location for it.

**Step 2.** On clicking the icon a new tab would open named AI-assistant so I would be creating a new exclusive tab for it.

**Step 3.** When that tab opens, the user will be able to provide a query; thus, following the tab, I will create an area where the user may send a query. That box would be accompanied with the send button.

**Step 4.** After configuring the send button, I would create two conversations, one from the user's side and one from the chatbot's side, and assign them the appropriate color, fonts, name, and dimensions.

**Step 5.** Once everything is created I would add things like scrollbar and other miscellaneous stuffs based on the needs.


### Figma Design-2
![](https://github.com/kshitijdshah99/Pippy_Activity/blob/main/Output/User%20Interface/FIGMA%20DESIGN-2.gif)

In this design I would be basically following this steps

**Step 1.** Choose an icon for the AI helper and place it in a convenient position.

**Step 2.** When the user clicks the icon, a side window opens up, displaying the code and terminal. Creating this side window would be my next step.

**Step 3.** When that side window opens, the user will be able to enter a query; thus, after the window, I will construct an area where the user may send a question. That box would be accompanied with the send button.

**Step 4.** After customizing the send button, I would start two chats, one from the user and one from the chatbot, and give them the proper color, fonts, name, and dimensions.

**Step 5.** Once everything has been done, I will add things like a scrollbar and other random necessities.

# Summary
With the complete 2 rough UI designs I completed with the setup of Sugar on my VM. After this I explored the Sugar's code repository to understand the import files that I need to modify.

At last I designed step-by-step roadmap for our developing the figma design we had discussed the previous week.

Once the design and approach is approved by the mentors I will start modifying the UI as per our needs.

# Plan for next week📝
Once the mentors gave me the go-ahead, I would begin building the user interface. Next week, I'll be delving further into Pippy's codebase and consulting with my mentors on how to make it consistent. 



