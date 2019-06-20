import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Stack;

/**
 * 155. Min Stack
 *
 * Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 *
 * push(x) -- Push element x onto stack.
 * pop() -- Removes the element on top of the stack.
 * top() -- Get the top element.
 * getMin() -- Retrieve the minimum element in the stack.
 *
 * Example:
 * MinStack minStack = new MinStack();
 * minStack.push(-2);
 * minStack.push(0);
 * minStack.push(-3);
 * minStack.getMin();   --> Returns -3.
 * minStack.pop();
 * minStack.top();      --> Returns 0.
 * minStack.getMin();   --> Returns -2.
 **/
class MinStack {

    private Stack<Integer> minStack;
    private Queue<Integer> minVals;

    /** initialize your data structure here. */
    public MinStack() {
        this.minStack = new Stack<>();
        this.minVals = new PriorityQueue<>();
    }

    public void push(int x) {
        minStack.push(x);
        minVals.offer(x);
    }

    public void pop() {
        int val = minStack.pop();
        if (val == minVals.peek())
            minVals.poll();
    }

    public int top() {
        return minStack.peek();
    }

    public int getMin() {
        return minVals.peek();
    }

    public static void main(String[] args) {
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        System.out.println(minStack.getMin());   // --> Returns -3.
        minStack.pop();
        System.out.println(minStack.top());      // --> Returns 0.
        System.out.println(minStack.getMin());  // --> Returns -2.
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */