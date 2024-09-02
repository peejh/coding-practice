// https://www.hackerrank.com/challenges/java-vistor-pattern
// Difficulty: MEDIUM
// Java 7

import java.util.*;
import java.util.Scanner;

enum Color {
    RED, GREEN
}

abstract class Tree {

    private int value;
    private Color color;
    private int depth;

    public Tree(int value, Color color, int depth) {
        this.value = value;
        this.color = color;
        this.depth = depth;
    }

    public int getValue() {
        return value;
    }

    public Color getColor() {
        return color;
    }

    public int getDepth() {
        return depth;
    }

    public abstract void accept(TreeVis visitor);
}

class TreeNode extends Tree {

    private ArrayList<Tree> children = new ArrayList<>();

    public TreeNode(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitNode(this);

        for (Tree child : children) {
            child.accept(visitor);
        }
    }

    public void addChild(Tree child) {
        children.add(child);
    }
}

class TreeLeaf extends Tree {

    public TreeLeaf(int value, Color color, int depth) {
        super(value, color, depth);
    }

    public void accept(TreeVis visitor) {
        visitor.visitLeaf(this);
    }
}

abstract class TreeVis
{
    public abstract int getResult();
    public abstract void visitNode(TreeNode node);
    public abstract void visitLeaf(TreeLeaf leaf);

}

class SumInLeavesVisitor extends TreeVis {
    
    private int result = 0;
    
    public int getResult() {
      	return this.result;
    }

    public void visitNode(TreeNode node) {
        return;
    }

    public void visitLeaf(TreeLeaf leaf) {
      	this.result += leaf.getValue();
    }
}

class ProductOfRedNodesVisitor extends TreeVis {
    
    private long result = 1L;
    
    public int getResult() {
      	return (int) this.result;
    }

    public void visitNode(TreeNode node) {
      	if (node.getColor() == Color.RED) {
            this.result *= node.getValue();
            this.result %= 1000000007;
        }
    }

    public void visitLeaf(TreeLeaf leaf) {
          if (leaf.getColor() == Color.RED) {
            this.result *= leaf.getValue();
            this.result %= 1000000007;
        }
    }
}

class FancyVisitor extends TreeVis {
    
    private int sumNode = 0;
    private int sumLeaf = 0;
    
    public int getResult() {
      	return Math.abs(this.sumNode - this.sumLeaf);
    }

    public void visitNode(TreeNode node) {
        if (node.getDepth() % 2 == 0)
            this.sumNode += node.getValue();
    }

    public void visitLeaf(TreeLeaf leaf) {
    	if (leaf.getColor() == Color.GREEN)
            this.sumLeaf += leaf.getValue();
    }
}

public class advanced_visitorPattern {
  
    public static Tree solve() {
        Scanner in = new Scanner(System.in);
        
        // Store the number of nodes
        int N = in.nextInt();
        
        // Store the value for each node
        int[] values = new int[N];
        for (int i = 0; i < N; i++) {
            values[i] = in.nextInt();
        }
        
        // Store the color for each node
        Color[] colors = new Color[N];
        for (int i = 0; i < N; i++) {
            colors[i] = in.nextInt() == 1 ? Color.GREEN : Color.RED;
        }
        
        // Store the edges
        Map<Integer, HashSet<Integer>> edges =  new HashMap<Integer, HashSet<Integer>>();
        for (int i = 0; i < N-1; i++) {
            int node1 = in.nextInt() - 1; // 1-based so turn into 0-based
            int node2 = in.nextInt() - 1;
            
            if (!edges.containsKey(node1)) {
                edges.put(node1, new HashSet<Integer>());
            }
            
            if (!edges.containsKey(node2)) {
                edges.put(node2, new HashSet<Integer>());
            }
            
            // Note that
            edges.get(node1).add(node2);
            edges.get(node2).add(node1);
        }
        
        // Create the node/leaf instances
        Tree[] nodes = new Tree[N];
        Stack<Integer> stack = new Stack<>(); // stack of indexes
        int depth = 0;
        stack.push(0);
              
        while (!stack.isEmpty()) {
            // Clear stack and store the indexes to a list
            List<Integer> currDepth = new ArrayList<>();            
            while (!stack.isEmpty()) {
                currDepth.add(stack.pop());
            }
            
            // For each parent index at current depth, create the
            // Tree instances either as TreeNode or TreeLeaf
            for (int p : currDepth) {          
                if (!edges.get(p).isEmpty()) {
                    nodes[p] = new TreeNode(values[p], colors[p], depth);
                    
                    // For each child index, push the index to the stack to
                    // be processed on the next depth/iteration
                    for (int c : edges.get(p)) {
                        stack.push(c);
                        // Remove the parent index from the child's set list
                        // to avoid cyclical paths
                        edges.get(c).remove(p);
                    }
                } else {
                    nodes[p] = new TreeLeaf(values[p], colors[p], depth);
                }
            }
            
            depth++;
        }
        
        // Attach parent nodes to its children nodes
        for (int p = 0; p < N; p++) {
            if (edges.containsKey(p)) {
                for (int c : edges.get(p)) {
                    ((TreeNode) nodes[p]).addChild(nodes[c]);
                }
            }
        }
        
        in.close();
        
        return (TreeNode) nodes[0];
    }

    public static void main(String[] args) {
      	Tree root = solve();
		SumInLeavesVisitor vis1 = new SumInLeavesVisitor();
      	ProductOfRedNodesVisitor vis2 = new ProductOfRedNodesVisitor();
      	FancyVisitor vis3 = new FancyVisitor();

      	root.accept(vis1);
      	root.accept(vis2);
      	root.accept(vis3);

      	int res1 = vis1.getResult();
      	int res2 = vis2.getResult();
      	int res3 = vis3.getResult();

      	System.out.println(res1);
     	System.out.println(res2);
    	System.out.println(res3);
	}
}